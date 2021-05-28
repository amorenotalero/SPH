from vpython import *

from particula import Particula
from sistemaParticulas import SistemaParticulas
import numpy as np

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

def generaCirculo(posicionInicial, masa, nCoronas, separacion, velocidadInicial, radio):
      """
      v1 = vector(1,0,0)
      v2 = rotate(v1, angle=pi/4, axis=vector(0,0,1))
      print(v1)
      print(v2)
      center = sphere(pos=vector(0,0,0),radius=0.25)
      vD= center.pos+vector(1,0,0)
      v90 = rotate(vD, angle=pi/2, axis=vector(0,0,1))
      vN90 = rotate(vD, angle=-pi/2, axis=vector(0,0,1))
      sphere(pos=v90,radius=0.25)
      sphere(pos=vN90,radius=0.25)
      """
      listaParticulas = SistemaParticulas()
      
      for corona in range(0,nCoronas,1):
            rad = (separacion+radio)*corona
            paso = 1
            if(corona!=0):
                  paso = 60/corona

            for alpha in np.arange(0,360,paso):
                  esferaCentro = Particula(posicionInicial,vector(0,0,0),radio,vector(0.79,0.95,1))
                  esferaCentro.setVelocidad(velocidadInicial)
                  esferaCentro.setMasa(masa)
                  posX = rad*cos(radians(alpha))
                  posY = esferaCentro.getPosY()
                  posZ = rad*sin(radians(alpha))
                  posicionModificada = posicionInicial + vector(posX,posY,posZ)
                  #print(posicionModificada)
                  esferaCentro.setPosicion(posicionModificada)
                  listaParticulas.addParticula(esferaCentro)
                  if(corona==0):
                        break
      
      return listaParticulas








