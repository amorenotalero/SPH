from __future__ import division, print_function

from vpython import *
import os


legal = {sphere:'sphere', box:'box', cylinder:'cylinder', distant_light:'distant_light', local_light:'local_light'}

ihat = vec(1, 0, 0)
jhat = vec(0, 1, 0)
khat = vec(0, 0, 1)
displayscale = 1.0 # global scale factor to adjust display.range to 100



def getpolar(a):
    # a is a vec
    # find rotation angles (standard polar coord)
    xy = sqrt(a.x**2 + a.y**2)
    theta = atan2(xy, a.z)
    phi = atan2(a.y, a.x)
    return [theta, phi]

def find_rotations(a):
    # find rotations
    theta, phi = getpolar(a.axis)
    # find rotation around x-axis (if a.up <> jhat)
    # "undo" theta & phi rotations so can find alpha
    aup = vec(a.up)
    aup = aup.rotate(axis=khat, angle=-phi)
    aup = aup.rotate(axis=jhat, angle=pi/2-theta)
    a_sin = dot(cross(jhat, norm(aup)), ihat)
    a_cos = dot(norm(aup), jhat)
    alpha = atan2(a_sin, a_cos)
    return (alpha, theta, phi)



def add_texture(a, code):
    # add in user-specified POV-ray texture (replaces color)
    tex = None
    if hasattr(a, 'pov_texture'):
        tex = a.pov_texture
    if tex:
        start = code.rfind('pigment {')
        end = start + code[start:].find('}') + 1
        code = code[:start] + tex + code[end:] 
    return code

def no_shadow(a):
    if hasattr(a,"no_shadow") and a.no_shadow:
        return "no_shadow"
    else:
        return ""

def no_reflection(a):
    if hasattr(a,"no_reflection") and a.no_reflection:
        return "no_reflection"
    else:
        return ""

def transparency(a):
    if hasattr(a,"opacity"):
        return 1-a.opacity
    else:
        return 0

def export_sphere(a):
    sphere_template = """
sphere {
    <%(posx)f, %(posy)f, %(posz)f>, %(radius)f
    texture {
        pigment {color rgbt <%(red)f, %(green)f, %(blue)f, %(transparency)f>}
        finish { phong %(shininess)f }
    }
    %(no_shadow)s
    %(no_reflection)s
}
"""
    object_code = sphere_template % { 'posx':displayscale*a.pos.x, 'posy':displayscale*a.pos.y, 'posz':displayscale*a.pos.z,
                                      'radius':displayscale*a.radius, 'shininess':0.6, 
                                      'red':a.red, 'green':a.green, 'blue':a.blue, 'transparency':transparency(a),
                                      'no_shadow':no_shadow(a), 'no_reflection':no_reflection(a)}
    object_code = add_texture(a, object_code)
    return object_code



def export_box(a):
    # create box at origin along x-axis
    # then rotate around x,y,z axes
    # then translate to final location
    box_template = """
box {
    <%(posx)f, %(posy)f, %(posz)f>, <%(pos2x)f, %(pos2y)f, %(pos2z)f>
    texture {
        pigment {color rgbt <%(red)f, %(green)f, %(blue)f, %(transparency)f>}
        finish { phong %(shininess)f }
    }
    rotate <%(rotx)f, %(roty)f, %(rotz)f>
    translate <%(transx)f, %(transy)f, %(transz)f>
    %(no_shadow)s
    %(no_reflection)s
}
"""
    alpha, theta, phi = find_rotations(a)
    # pos of box is at center
    # generate two opposite corners for POV-ray
    pos1 = displayscale*(-a.size/2)
    pos2 = displayscale*( a.size/2)

    object_code = box_template % { 'posx':pos1.x, 'posy':pos1.y, 'posz':pos1.z,
                                   'pos2x':pos2.x, 'pos2y':pos2.y, 'pos2z':pos2.z,
                                   'rotx':alpha*180/pi, 'roty':-90+theta*180/pi, 'rotz':phi*180/pi,
                                   'transx':displayscale*a.pos.x, 'transy':displayscale*a.pos.y, 'transz':displayscale*a.pos.z,
                                   'red':a.red, 'green':a.green, 'blue':a.blue, 'transparency':transparency(a),
                                   'shininess':0.6,
                                   'no_shadow':no_shadow(a), 'no_reflection':no_reflection(a) }
    object_code = add_texture(a, object_code)
    return object_code

def export_cylinder(a):
    cylinder_template = """
cylinder {
    <%(posx)f, %(posy)f, %(posz)f>,<%(pos2x)f, %(pos2y)f, %(pos2z)f>, %(radius)f
    texture {
        pigment {color rgbt <%(red)f, %(green)f, %(blue)f, %(transparency)f>}
        finish { phong %(shininess)f }
    }
    %(no_shadow)s
    %(no_reflection)s
}
"""
    endpt1=displayscale*a.pos
    endpt2=displayscale*(a.pos+a.axis)
    object_code = cylinder_template % { 'posx':endpt1.x, 'posy':endpt1.y, 'posz':endpt1.z,
                                        'pos2x':endpt2.x, 'pos2y':endpt2.y, 'pos2z':endpt2.z,
                                        'red':a.red, 'green':a.green, 'blue':a.blue, 'transparency':transparency(a),
                                        'radius':displayscale*a.radius, 'shininess':0.6,
                                        'no_shadow':no_shadow(a), 'no_reflection':no_reflection(a) }
    object_code = add_texture(a, object_code)
    return object_code









def export(canvas=None, filename=None, include_list=None, custom_text='', shadowless=0):
    canv = canvas

    global displayscale
    if canv == None:         # no display specified so find active display
        b = box(visible=0)
        canv = b.canvas

    if filename == None:
        if len(canv.title) == 0: filename = 'povray.pov'
        else: filename = canv.title + '.pov'

    if include_list == None:
        include_text = ''
        # Maybe should always include the following definitions?
        #include_text = '#include "colors.inc"\n#include "stones.inc"\n#include "woods.inc"\n#include "metals.inc"\n'
    else:
        include_text = '\n'
        for x in include_list:
            include_text = include_text + '#include "'+ x + '"\n'

    initial_comment = """// POV-ray code generated by povexport.py
"""


    ambient_template = """
global_settings { ambient_light rgb <%(red)f, %(green)f, %(blue)f> }
"""

    scalar_ambient_template = """
global_settings { ambient_light rgb <%(amb)f, %(amb)f, %(amb)f> }
"""

    background_template = """
background { color rgb <%(red)f, %(green)f, %(blue)f> }
"""

    light_template = """
light_source { <%(posx)f, %(posy)f, %(posz)f>
    color rgb <%(red)f, %(green)f, %(blue)f>
}
"""

    camera_template = """
camera {
    right <-image_width/image_height, 0, 0>      // vpython uses right-handed coord. system
    location <%(posx)f, %(posy)f, %(posz)f>
    up <%(upx)f, %(upy)f, %(upz)f>
    look_at <%(pos2x)f, %(pos2y)f, %(pos2z)f>
    angle %(fov)f
}
"""

    # begin povray setup
    file = open(filename, 'w')
    print(os.path.realpath(file.name))

    file.write( initial_comment + include_text + custom_text)
    file.write( ambient_template % { 'red':canv.ambient.x*10 ,
                                         'green':canv.ambient.y*10,
                                         'blue':canv.ambient.z*10 })
    file.write( background_template % { 'red':canv.background.x,
                                        'green':canv.background.y,
                                        'blue':canv.background.z } )

    displayscale = 10/canv.range # deal with very small range values (e.g. atomic sizes)

    for light in canv.lights: # reproduce vpython lighting (not ideal, but good approximation)
        if type(light) is distant_light:
            pos = norm(light.direction) * 1000 # far away to simulate parallel light
        elif type(light) is local_light:
            pos = displayscale*light.pos
        lcolor = light.color
        light_code = light_template % { 'posx':pos.x, 'posy':pos.y, 'posz':pos.z,
                                        'red':lcolor.x, 'green':lcolor.y, 'blue':lcolor.z }
        if shadowless:
            end = light_code.rfind('}')
            light_code = light_code[:end] + '    shadowless\n' + light_code[end:]
        file.write( light_code )

    #modificado para misma camara siempre
    file.write( camera_template % { 'posx':7.5, 'posy':7.5, 'posz':83.5,
                                    'upx':0.0, 'upy':1.0, 'upz':0.0,
                                    'pos2x':5.0, 'pos2y':5.0, 'pos2z':5.0,
                                    'fov':60.0 } )

    for obj in canv.objects:
        key = obj.__class__
        if key in legal:
            obj_name = legal[key]
            if obj_name == 'distant_light' or obj_name == 'local_light': continue
            function_name = 'export_' + obj_name
            function = globals().get(function_name)
            object_code = function(obj)
            if object_code is None:
                continue
            file.write( object_code )
        else:
            print('WARNING: export function for ' + str(obj.__class__) + ' not implemented')

    file.close()
    return 'The export() function no longer returns the display as an\n' \
           'endless POV-Ray string, but saves it to a file instead.'
# end defining export()

