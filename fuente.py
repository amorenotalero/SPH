from vpython import *

from particula import Particula
from sistemaParticulas import SistemaParticulas

def generaColumna(posicionInicial, masa, numParticulasX, numParticulasY, numParticulasZ, separacion, velocidadInicial, radio):
    
    listaParticulas = SistemaParticulas()


    for k in range(numParticulasZ):
          valor = 0.0
          for j in range(numParticulasY):
                for i in range(numParticulasX):
                      p = Particula(posicionInicial,vector(0,0,0),radio,vector(0.79,0.95,1))
                      p.setVelocidad(velocidadInicial)
                      if(k%2==0):
                            valor = 0.1
                      else:
                            valor = 0.0
                      control = 1.0+valor
                      posicionModificada = posicionInicial+(vector(i*control,j,k)*separacion)
                      p.setPosicion(posicionModificada)
                      listaParticulas.addParticula(p)
    return listaParticulas
