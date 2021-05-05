from vpython import *

from particula import Particula

class SistemaParticulas:
    def __init__(self):
        
        particulas = []
        self.listaParticulas = particulas
    def getNumParticulas(self):
        cont = 0
        for p in self.listaParticulas:
            cont = cont + 1
        return cont
    def addParticula(self,particula):
        self.listaParticulas.append(particula)
        return self.listaParticulas
    def getParticula(self,index):
        particula = self.listaParticulas[index]
        return particula
    def getParticulas(self):
        return self.listaParticulas

    def getIndex(self, particula):
        index = self.listaParticulas.index(particula)
        return index
    def changeParticula(self, index, particula):
        self.listaParticulas[index]=particula

