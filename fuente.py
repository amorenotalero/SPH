from vpython import *

from particula import Particula
from sistemaParticulas import SistemaParticulas

def generaColumna(posicionInicial, masa, numParticulasX, numParticulasY, numParticulasZ, separacion, velocidadInicial, radio):
    
    listaParticulas = SistemaParticulas()


    for k in range(numParticulasZ):
          for j in range(numParticulasY):
                for i in range(numParticulasX):
                      p = Particula(posicionInicial,vector(0,0,0),radio,vector(0.79,0.95,1))
                      p.setVelocidad(velocidadInicial)
                      p.setMasa(masa)
                      if(j==0):
                            controlX = i+0.1#modifica el primer estrato para moverlo hacia la derecha y que no reboten sobre ellas
                            controlZ = k+0.1
                      else:
                            controlX = i
                            controlZ = k
                      posicionModificada = posicionInicial+(vector(controlX,j,controlZ)*separacion)
                      p.setPosicion(posicionModificada)
                      listaParticulas.addParticula(p)
    return listaParticulas
