from vpython import *

def MetodoEuler(posicion, velocidad, aceleracion, tiempo):
    vn_1x = velocidad.x + aceleracion.x*tiempo
    #if(vn_1x > 4.5):
    #    vn_1x = vn_1x*0.84
    vn_1y = velocidad.y + aceleracion.y*tiempo
    if(vn_1y > 4.5):
        vn_1y = vn_1y*0.84
    vn_1z = velocidad.z + aceleracion.z*tiempo
    #if(vn_1z > 4.5):
    #    vn_1z = vn_1z*0.84
    rn_1x = posicion.x + vn_1x*tiempo + (aceleracion.x*tiempo*tiempo)/2 
    rn_1y = posicion.y + vn_1y*tiempo + (aceleracion.y*tiempo*tiempo)/2
    rn_1z = posicion.z + vn_1z*tiempo + (aceleracion.z*tiempo*tiempo)/2
    vn_1 = vector(vn_1x,vn_1y,vn_1z)
    rn_1 = vector(rn_1x,rn_1y,rn_1z)
    res = [rn_1,vn_1]
    return res
