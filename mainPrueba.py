
from vpython import *
from sistemaParticulas import *
from particula import *
import fuente
import exportadorBIN_RF

primerExportador = "Prueba"

particula = Particula(vector(1.0,0.0,0.0),vector(0.0,0.0,0.0),0.5)
sistema = SistemaParticulas()
sistema.addParticula(particula)
numParticulasX = 10
numParticulasY  = 10
numParticulasZ = 5
posicionInicial = vector(-0.5,0.0, -0.5)
velocidadInicial = vector(0.0,0.0,0.0)
fluido = fuente.generaColumna(posicionInicial, 0.1, numParticulasX, numParticulasY, numParticulasZ, 0.17, velocidadInicial, 0.5)


exportadorBIN_RF.exportar(primerExportador,5,fluido,0.5)


