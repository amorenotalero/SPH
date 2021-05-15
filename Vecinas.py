from vpython import *

from particula import Particula
from sistemaParticulas import SistemaParticulas

def vecinas(SistemaParticulas, distancia):
    numParticulas = SistemaParticulas.getNumParticulas()
    for i in range(numParticulas):
        for j in range(numParticulas):
            if(i != j):
                pi = SistemaParticulas.getParticula(i)
                pj = SistemaParticulas.getParticula(j)
                vectorDistanciaParticulas = pj.getPosicion()-pi.getPosicion()
                distanciaParticulas = mag(vectorDistanciaParticulas)
                if distanciaParticulas <= distancia:
                    pi.addVecina(j)
                    SistemaParticulas.changeParticula(i,pi)

                
def clearVecinas(SistemaParticulas):
    for p in SistemaParticulas.getParticulas():
        vacia = []
        p.setListaVecinas(vacia)
        