from vpython import *

from particula import Particula

def detectaColisionLimites(LimitesX, LimitesY, LimitesZ, espesor, particula):
    posicion = particula.getPosicion()
    LimX_inf = LimitesX[0] + espesor
    LimX_sup = LimitesX[1] - espesor
    LimY_inf = LimitesY[0] + espesor
    LimY_sup = LimitesY[1] - espesor
    LimZ_inf = LimitesZ[0] + espesor
    LimZ_sup = LimitesZ[1] - espesor
    
    normal_x = vector(1.0,0.0,0.0)
    normal_y = vector(0.0,1.0,0.0)
    normal_z = vector(0.0,0.0,1.0)

    vectorNormal = vector(0.0, 0.0, 0.0)
    
    colisionLimX = posicion.x < LimX_inf or posicion.x > LimX_sup 
    colisionLimY = posicion.y < LimY_inf or posicion.y > LimY_sup
    colisionLimZ = posicion.z < LimZ_inf or posicion.z > LimZ_sup
    if colisionLimX:
        if posicion.x > LimX_sup:
            #particula.setEstadoColision(True)
            normal_x = -1*normal_x
            vectorNormal = vectorNormal + normal_x
        else:
            #particula.setEstadoColision(True)
            vectorNormal = vectorNormal + normal_x

        particula.setEstadoColision(True)

    if colisionLimY:
        if posicion.y < LimY_inf:
            #particula.setEstadoColision(True)
            vectorNormal = vectorNormal + normal_y
            particula.setEstadoColision(True)

        #Le he quitado el else para que la caja este abierta
        

    if colisionLimZ:
        
        if posicion.z > LimZ_sup:
            #particula.setEstadoColision(True)
            normal_z = -1*normal_z
            vectorNormal = vectorNormal + normal_z
        else:
            #particula.setEstadoColision(True)
            vectorNormal = vectorNormal + normal_z

        particula.setEstadoColision(True)

    return vectorNormal
    #if(particula.getEstadoColision()==True):
        #particula.setEstadoSPH()
        
    #    respuestaColision(particula,vectorNormal,espesor)


def detectaColisionEsfera(centro, radio,espesor, particula):
    vectorNormal = vector(0.0, 0.0, 0.0)
    vectorDistancia = particula.getPosicion()-centro 
    distancia = mag(vectorDistancia)
    radio = radio + espesor
    if distancia < radio:
        particula.setEstadoColision(True)
        #respuestaColision(particula, vectorDistancia)
        vectorNormal = vectorNormal + vectorDistancia
    return vectorNormal

def detectaColisionCilindro(LimiteY, eje, espesor, radio, particula):
    vectorNormal = vector(0.0, 0.0, 0.0)
    posicionPart = particula.getPosicion()
    LimiteY_inf = LimiteY[0] + espesor
    LimiteY_sup = LimiteY[1] - espesor
    colisionLimY = posicionPart.y < LimiteY_inf or posicionPart.y > LimiteY_sup
    vectorDistancia = posicionPart - vector(eje.x,posicionPart.y,eje.z)
    distancia = mag(vectorDistancia)
    radio = radio + espesor
    fueraRadio = distancia < radio
    if(colisionLimY or fueraRadio):
        if(posicionPart.y < LimiteY_inf):
            particula.setEstadoColision(True)
            vectorNormal = vectorNormal+eje
        if posicionPart.y > LimiteY_sup:
            particula.setEstadoColision(True)
            vectorNormal = vectorNormal-eje
        if fueraRadio:
            particula.setEstadoColision(True)
            vectorNormal = vectorNormal + vectorDistancia
    return vectorNormal

def colisionMultiple(particula,caja,esfera,cilindro):
    vectorNormal = vector(0.0, 0.0, 0.0)
    if(esfera!=[]):
        centro = esfera[0]
        radio = esfera[1]
        espesor = esfera[2]
        vectorEsfera = detectaColisionEsfera(centro, radio,espesor, particula)
        vectorNormal = vectorNormal + vectorEsfera
    if(caja!=[]):
        LimitesX = caja[0]
        LimitesY = caja[1]
        LimitesZ = caja[2]
        espesor = caja[3]
        vectorCaja = detectaColisionLimites(LimitesX, LimitesY, LimitesZ, espesor, particula)
        vectorNormal = vectorNormal + vectorCaja
    
    if(cilindro!=[]):
        LimiteY = cilindro[0]
        eje = cilindro[1]
        espesor = cilindro[2]
        radio = cilindro[3]
        vectorCilindro = detectaColisionCilindro(LimiteY, eje, espesor, radio, particula)
        vectorNormal = vectorNormal + vectorCilindro
    if(particula.getEstadoColision()==True):
        respuestaColision(particula,vectorNormal,espesor)

    

            

    

def detectaColisionTriangulo(triangulo, particula):
    colisiona = False
    verticeA = triangulo[0]
    verticeB = triangulo[1]
    verticeC = triangulo[2]
    posicionPart = particula.getPosicion()
    vectorAB = verticeB - verticeA
    vectorAC = verticeC - verticeA
    productoVectorial = cross(vectorAB,vectorAC)
    superficie = mag(productoVectorial)
    vectorAP = posicionPart - verticeA
    productoMixto = dot(vectorAP,productoVectorial)
    volumen = mag(productoMixto)
    altura = volumen/superficie
    if(altura < 0.49):
        Sx = productoVectorial.x
        Sy = productoVectorial.y
        Sz = productoVectorial.z
        partProyectadaX = (posicionPart.x + altura/superficie)*Sx
        partProyectadaY = (posicionPart.y + altura/superficie)*Sy
        partProyectadaZ = (posicionPart.z + altura/superficie)*Sz
        partProyectada = vector(partProyectadaX,partProyectadaY,partProyectadaZ)
        vectorPpA = partProyectada - verticeA
        vectorPpB = partProyectada - verticeB
        vectorPpC = partProyectada - verticeC
        productoEscalarPpA_PpB = dot(vectorPpA,vectorPpB)
        productoEscalarPpB_PpC = dot(vectorPpB,vectorPpC)
        productoEscalarPpC_PpA = dot(vectorPpC,vectorPpA)
        magnitudPpA = mag(vectorPpA)
        magnitudPpB = mag(vectorPpB)
        magnitudPpC = mag(vectorPpC)

        angulo1 = acos(productoEscalarPpA_PpB/(magnitudPpA*magnitudPpB))
        angulo2 = acos(productoEscalarPpB_PpC/(magnitudPpB*magnitudPpC))
        angulo3 = acos(productoEscalarPpC_PpA/(magnitudPpC*magnitudPpA))
        sumaAngulos = angulo1 + angulo2 + angulo3 
        if sumaAngulos == 2*pi:#si no funciona hay que cambiar el igual por un limite de error |-| 2pi-0.2 < sumaAngulos < 2pi+0.2 
            colisiona = True
            vectorNormalTriangulo = cross(vectorAB,vectorAC)
            respuestaColision(particula,vectorNormalTriangulo)
            


        

def respuestaColision(particula, vectorNormal, espesor):
    tasaRebote = 0.8
    tasaRozamineto = 0.98
    tasaPenetracion = 0.005*espesor
    Vinicial = particula.getVelocidad()
    posicion_incidente = particula.getPosicion()
    velocidadInicialNormal = proj(Vinicial,vectorNormal)
    velocidadInicialTangencial = Vinicial - velocidadInicialNormal
    velocidadFinalNormal = -(tasaRebote*velocidadInicialNormal)
    velocidadFinalTangencial = tasaRozamineto*velocidadInicialTangencial
    velocidadFinal = velocidadFinalNormal + velocidadFinalTangencial
    particula.setVelocidad(velocidadFinal)
    tolerancia_posicion = tasaPenetracion*vectorNormal
    posicion_final = posicion_incidente + tolerancia_posicion
    particula.setPosicion(posicion_final)
