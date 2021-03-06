from vpython import *
from particula import *
from sistemaParticulas import *
from dinamica import *
import sys
#-------------------
import gestorColision
import metodoIntegracion
#import operacionesVectoriales
import fuente
import vecinosHash
import Vecinas


print("inicio sistema")


#Implementacion de la ventana de simulacion

scene = canvas(title="SPH", width=500, height=500, x=0, y=0, center = vector(1./2.,1./2.,1./2.), forward = vector(129.620536, 3.904938, 123.748005), background=color.white )
scene.autoscale = False

scene.forward # position
scene.center # look up


#Generar contenedor con el que colisiona las particulas.
caja = box(pos=vector(0.0,0.0,0.0), length=5, height=3, width=2.0)
caja.opacity = 0.1

#Se genera un objeto de colision y a ese objeto se le pasa para como parametro la caja

#-----------------------------
#Limites de X
posicionX = caja.pos.x
LimSupX = posicionX + (0.5*caja.length)
LimInfX = posicionX - (0.5*caja.length)
LimitesX = [LimInfX,LimSupX]    
#Limites de Y
posicionY = caja.pos.y
LimSupY = posicionY + (0.5*caja.height)
LimInfY = posicionY - (0.5*caja.height)
LimitesY = [LimInfY,LimSupY]
#Limites de Z
posicionZ = caja.pos.z
LimSupZ = posicionZ + (0.5*caja.width)
LimInfZ = posicionZ - (0.5*caja.width)
LimitesZ = [LimInfZ,LimSupZ]

espesor = 0.06#cota de tolerancia a la colision
tasaAmortiguamiento = 0.8 #tasa amortiguamiento en la colision
#-----------------------------


#-----------------------------
#-----GeneraParticulas--------
#-----------------------------

masa = 0.1
radio = 0.04
h = 0.18 #radio dominio soportado
separacion = 0.17 #1.08*h
numParticulasX = 5
numParticulasY  = 5
numParticulasZ = 5
posicionInicial = vector(-0.5,0.0, -0.5)
#velocidadInicial = vector(0.2,-4.0,0.5)
velocidadInicial = vector(0,0,0)
#Generar fuente de columna cuadrada
fluido = fuente.generaColumna(posicionInicial, masa, numParticulasX, numParticulasY, numParticulasZ, separacion, velocidadInicial, radio)

numeroParticulas = fluido.getNumParticulas()
print("eeeeeeeeoooo   "+str(numeroParticulas))
#----------------------------------------------------------

#Calcular fuerzas internas con la clase dinamica 
dinamica = Dinamica(fluido, h)

#dinamicaEstable = DinamicaEstable(fluido, separacion)

#Calcular fuerza externa, en este caso solo hay gravedad
aceleracion = vector(0.0,-9.81, 0.0)
#fuerzaExterna = operacionesVectoriales.escalarVector(masa,aceleracion) 
fuerzaExterna = aceleracion*masa 
#fuerzaExterna = vector(0,0,0)
#--------------------------------------------------------------
#Variables para el bucle de simulacion.

K = -180
pasoTiempo = 0.001
cont = 0

#parte iterativa del bucle de simulacion

while cont < 6000:
    rate(100)
    
    print ('Estoy en el paso: '+repr(cont))
    
    #Calcula vecinas.
    #vecinosHash.calculaVecinas(fluido,h)
    Vecinas.clearVecinas(fluido)
    vecinosHash.calculaVecinosHash(fluido,h)
    #Vecinas.clearVecinas(fluido)
    #Vecinas.vecinas(fluido,h)
    

    #Calcula la fuerza interna para todo el sistema
    fuerzas = dinamica.fuerzas(K)
    #print(fuerzas)
   
    for i in range(numeroParticulas):
        particula_i = fluido.getParticula(i)
        gestorColision.detectaColisionLimites(LimitesX, LimitesY, LimitesZ, espesor, particula_i)
        if (particula_i.getEstadoColision() == True):
            #la particula ha colisionado
            particula_i.setEstadoColision(False)
        else:
            velocidadParticula = particula_i.getVelocidad()
            posicionParticula = particula_i.getPosicion()
            #obtengo fuerzas internas que calcule en la clase dinamica.
            fuerzasInternas = particula_i.getFuerzas()
            #print(fuerzasInternas)
            fuerzaNeta = fuerzasInternas + fuerzaExterna
            #aceleracion = operacionesVectoriales.escalarVector((1.0/masa),fuerzaNeta)
            aceleracion = (1.0/masa)*fuerzaNeta
            
            nuevaCinematica = metodoIntegracion.MetodoEuler(posicionParticula, velocidadParticula, aceleracion, pasoTiempo)
            particula_i.setPosicion(nuevaCinematica[0])
            particula_i.setVelocidad(nuevaCinematica[1])
            fluido.changeParticula(i,particula_i)
    cont+=1

print("Simulacion Concluida")
sys.exit()






    

