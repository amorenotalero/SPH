from vpython import *


def Funcionkernel(h,r):
    h7 = h*h*h*h*h*h*h
    h2 = h*h
    r2 = r*r
    alfa = 1.08*h2
    parteFraccion = (alfa*315.0)/(64.0*pi*h7)
    parteResta = (h2-r2)
    parteAlcubo = parteResta*parteResta*parteResta
    Wij = parteFraccion*parteAlcubo
    return Wij

def GradientKernel(h,r,rVector):
    h5 = h*h*h*h*h
    r2 = r*r
    h2 = h*h
    beta = 1.768*h
    parteFraccion = (beta*15.0)/(pi*h5)
    parteResta = (h2-r2)
    parteAlCuadrado = parteResta*parteResta
    rAcento = norm(rVector)
    GradienteWij = parteFraccion*parteAlCuadrado*rAcento
    return GradienteWij

def LaplacianoKernel(h,r):
    ganma = 31.16
    h2 = h*h
    r2 = r*r
    parteFraccion = (ganma*318.0)/(7.0*pi*h2)
    parteResta = h2-r2
    LaplacianoWij = parteFraccion*parteResta
    return LaplacianoWij






