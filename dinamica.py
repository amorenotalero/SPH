from vpython import *

from particula import Particula
from sistemaParticulas import SistemaParticulas
import kernel

class Dinamica():
    def __init__(self, fluido, h):
        self.fluido = fluido
        self.h = h

    def fuerzas(self,K):
        Fluido = self.fluido
        h = self.h
        numParticulas = Fluido.getNumParticulas()
         
        for i in range(numParticulas):
            pi = Fluido.getParticula(i)
            vecinas = pi.getVecinas()
            sumatorio = vector(0,0,0)
            for j in vecinas:
                pj = Fluido.getParticula(j)
                ri = pi.getPosicion()
                rj = pj.getPosicion()
                resta_rj_ri = rj - ri
                magnitudResta = mag(resta_rj_ri)
                parteEscalar = magnitudResta - h
                parteVectorial = norm(resta_rj_ri)
                ecuacion = parteEscalar*parteVectorial
                sumatorio = ecuacion + sumatorio
            
            fuerzaij = (K)*sumatorio
            pi.setFuerza(fuerzaij)
            Fluido.changeParticula(i,pi)
        self.fluido = Fluido
  
    def fuerzasSPH(self,K,nu):
        Fluido = self.fluido
        h = self.h
        numParticulas = Fluido.getNumParticulas()
         
        for i in range(numParticulas):
            pi = Fluido.getParticula(i)
            vecinas = pi.getVecinas()
            sumatorioFuerzaPresion = vector(0.0,0.0,0.0)
            sumatorioFuerzaViscosidad = vector(0.0,0.0,0.0)
            for j in vecinas:                
                pj = Fluido.getParticula(j)
                ri = pi.getPosicion()
                rj = pj.getPosicion()
                vectorDistancia =  rj - ri
                magnitudDistancia = mag(vectorDistancia)
                vi = pi.getVelocidad()
                vj = pj.getVelocidad()
                di = pi.getDensidad()
                dj = pj.getDensidad()
                mj = pj.getMasa()
                #Ecuacion fuerza de presion
                gradienteKernel = kernel.GradientKernel(h,magnitudDistancia,vectorDistancia)
                maximaDensidad = max(di,dj)
                ecuacionPresion = mj*((di+dj)/(2.0*maximaDensidad))*gradienteKernel

                sumatorioFuerzaPresion = ecuacionPresion + sumatorioFuerzaPresion

                #Ecuacion fuerza de viscosidad
                laplacianoKernel = kernel.LaplacianoKernel(h,magnitudDistancia)
                restaVelocidad =vi-vj
                ecuacionViscosidad = mj*restaVelocidad*0.5*laplacianoKernel
                
                sumatorioFuerzaViscosidad = ecuacionViscosidad + sumatorioFuerzaViscosidad

            fuerzaPresion = (-K)*sumatorioFuerzaPresion
            fuerzaViscosidad = nu*sumatorioFuerzaViscosidad
            fuerzas = fuerzaPresion-fuerzaViscosidad
            pi.setFuerza(fuerzas)
            Fluido.changeParticula(i,pi)
        self.fluido = Fluido

    def DensidadMasa(self):
        Fluido = self.fluido
        h = self.h
        numParticulas = Fluido.getNumParticulas()
        for i in range(numParticulas):
            pi = Fluido.getParticula(i)
            vecinas = pi.getVecinas()
            sumatorio = 0
            for j in vecinas:
                pj = Fluido.getParticula(j)
                ri = pi.getPosicion()
                rj = pj.getPosicion()
                vectorDistancia =  rj - ri
                magnitudDistancia = mag(vectorDistancia)
                funcionKernel = kernel.Funcionkernel(h,magnitudDistancia)
                
                sumatorio = pj.getMasa()*funcionKernel + sumatorio
            pi.setDensidad(sumatorio)
            Fluido.changeParticula(i,pi)
        self.fluido = Fluido




