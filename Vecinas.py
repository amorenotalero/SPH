from vpython import *

from particula import Particula
from sistemaParticulas import SistemaParticulas

def vecinas(SistemaParticulas, distancia):
    numParticulas = SistemaParticulas.getNumParticulas()
    #ListadoVecinas = {}
    for i in range(numParticulas):
        for j in range(numParticulas):
            if(i != j):
                pi = SistemaParticulas.getParticula(i)
                pj = SistemaParticulas.getParticula(j)
                vectorDistanciaParticulas = pj.getPosicion()-pi.getPosicion()
                distanciaParticulas = mag(vectorDistanciaParticulas)
                #print("Distancia particulas")
                #print(distanciaParticulas)
                #print("Distancia")
                #print(distancia)
                if distanciaParticulas <= distancia:
                    #ListadoVecinas["N("+str(i)+")"] = j
                    pi.addVecina(j)
                    SistemaParticulas.changeParticula(i,pi)
                    #print("----Clase vecina----")
                    #print(pi.getVecinas())

    #return ListadoVecinas
                
def clearVecinas(SistemaParticulas):
    for p in SistemaParticulas.getParticulas():
        vacia = []
        p.setListaVecinas(vacia)
        