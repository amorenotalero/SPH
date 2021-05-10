from vpython import *


def Funcionkernel(h,r):
    h7 = pow(h,7)
    h2 = h*h
    r2 = r*r
    alfa = 1.08*h2
    parteFraccion = alfa*315/64*pi*h7
    parteResta = h2-r2
    parteAlcubo = pow(parteResta,3)
    Wij = parteFraccion*parteAlcubo
    return Wij

def GradientKernel(h,r):
    h5 = pow(h,5)
    r2 = r*r
    h2 = h*h
    beta = 1.768*h
    parteFraccion = beta*15/pi*h5
    parteResta = h2-r2
    parteAlCuadrado = parteResta*parteResta
    rAcento = r
    GradienteWij = parteFraccion*parteAlCuadrado*rAcento
    return GradienteWij

def LaplacianoKernel(h,r):
    ganma = 31.16
    h2 = h*h
    r2 = r*r
    parteFraccion = gamma*318/7*pi*h2
    parteResta = h2-r2
    LaplacianoWij = parteFraccion*parteResta
    return LaplacianoWij






