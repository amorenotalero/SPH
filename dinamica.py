from vpython import *

from particula import Particula
from sistemaParticulas import SistemaParticulas
import fuente
import Vecinas
import kernel

class Dinamica():
    def __init__(self, fluido, h):
        self.fluido = fluido
        self.h = h

    def fuerzas(self,K):
        Fluido = self.fluido
        h = self.h
        numParticulas = Fluido.getNumParticulas()
        #print(numParticulas)
        ListadoFuerzas = {}
         
        for i in range(numParticulas):
            pi = Fluido.getParticula(i)
            vecinas = pi.getVecinas()
            #print("----Lista de vecina en clase dinamica-------")
            #print(vecinas)
            #numVecinas = len(vecinas)
            #print("----------Particula"+str(i)+"---------------")
            sumatorio = vector(0,0,0)
            for j in vecinas:
                #print(j)
                pj = Fluido.getParticula(j)
                ri = pi.getPosicion()
                rj = pj.getPosicion()
                #print("Vector posicion particula 1")
                #print(ri)
                #print("Vector posicion particula 2")
                #print(rj)
                resta_rj_ri = rj - ri
                magnitudResta = mag(resta_rj_ri)
                #print(magnitudResta)
                parteEscalar = magnitudResta - h
                parteVectorial = norm(resta_rj_ri)
                ecuacion = parteEscalar*parteVectorial
                sumatorio = ecuacion + sumatorio
            
            fuerzaij = (-K)*sumatorio
            #print(fuerzaij)
            pi.setFuerza(fuerzaij)
            Fluido.changeParticula(i,pi)
        self.fluido = Fluido
            #f = pi.getFuerzas()
            #print(f)
"""   
    def fuerzasSPH(self,K,nu):
        Fluido = self.fluido
        h = self.h
        numParticulas = Fluido.getNumParticulas()
        #print(numParticulas)
         
        for i in range(numParticulas):
            pi = Fluido.getParticula(i)
            vecinas = pi.getVecinas()
            #print("----Lista de vecina en clase dinamica-------")
            #print(vecinas)
            #numVecinas = len(vecinas)
            #print("----------Particula"+str(i)+"---------------")
            for j in vecinas:
                #recorre demasiado las listas simplificar codigo
                DensidadMasa()
                fuerzaPresion = FuerzaPresion()
                fuerzaViscosidad = FuerzaViscosidad(nu)



                

            
            fuerzaij = (-K)*sumatorio
            #print(fuerzaij)
            pi.setFuerza(fuerzaij)
            Fluido.changeParticula(i,pi)
            self.fluido = Fluido
            #f = pi.getFuerzas()
            #print(f)

    def DensidadMasa(self):
        Fluido = self.fluido
        h = self.h
        numParticulas = Fluido.getNumParticulas()
        for i in range(numParticulas):
            pi = Fluido.getParticula(i)
            vecinas = pi.getVecinas()
            sumatorio = 0
            for j in vecinas:
                #print(j)
                pj = Fluido.getParticula(j)
                ri = pi.getPosicion()
                rj = pj.getPosicion()
                vectorDistancia =  rj - ri
                magnitudDistancia = mag(vectorDistancia)
                sumatorio = pj.getMasa()*kernel.Funcionkernel(h,magnitudDistancia) + sumatorio
            pi.setDensidad(sumatorio)
            Fluido.changeParticula(i,pi)
            self.fluido = Fluido
    
    def FuerzaPresion





"""
                
"""        
masa = 0.1
radio = 0.04
h = 0.18 #radio dominio soportado
separacion = 0.17 #1.08*h
numParticulasX = 2
numParticulasY = 1
numParticulasZ = 1
posicionInicial = vector(-0.5,0.0, -0.5)
#velocidadInicial = vector(0.2,-4.0,0.5)
velocidadInicial = vector(0,0,0)
#Generar fuente de columna cuadrada
fluido = fuente.generaColumna(posicionInicial, masa, numParticulasX, numParticulasY, numParticulasZ, separacion, velocidadInicial, radio)
dinamica = Dinamica(fluido, h)
K = -180
pasoTiempo = 0.001
cont = 0
while cont < 10:
    rate(100)
    Vecinas.clearVecinas(fluido)
    Vecinas.vecinas(fluido,h)
    print("numero de particulas")
    print(fluido.getNumParticulas())
    p = fluido.getParticula(0);
    print("vecinas de p")
    print(p.getVecinas())
    print("particulas en fluido")
    print(fluido.getParticulas())
    fuerzas = dinamica.fuerzas(K)
    cont+=1
"""




