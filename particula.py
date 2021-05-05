from vpython import *





class Particula:    
    def __init__(self, posicion, velocidad, radio, color=None ):
        self.posicion = posicion
        self.velocidad = velocidad
        self.radio = radio
        self.vecinas = []
        self.fuerzas = vector(0,0,0)
        self.estadoColision = False
        if (color is None):
            self.color = vector(0,0,1)
        else:
            self.color = color
        self.body = sphere(pos=self.posicion, radius=self.radio, velocity=self.velocidad, color=self.color)

    def getPosicion(self):
        return self.body.pos

    def getPosX(self):
        return self.body.pos.x

    def getPosY(self):
        return self.body.pos.y
       
    def getPosZ(self):
        return self.body.pos.z

    def getVelocidad(self):
        return self.body.velocity

    def getVelX(self):
        return self.body.velocity.x

    def getVelY(self):
        return self.body.velocity.y

    def getVelZ(self):
        return self.body.velocity.z

    def getRadio(self):
        return self.radio

    def getColor(self):
        return self.body.color

    def setPosicion(self, posicion):
        self.body.pos = posicion

    def setPosX(self, x):
        self.body.pos.x = x

    def setPosY(self, y):
        self.body.pos.y = y

    def setPosZ(self, z):
        self.body.pos.z = z

    def setVelocidad(self, velocidad):
        self.body.velocity = velocidad

    def setVelX(self, vx):
        self.body.velocity.x = vx

    def setVelY(self, vy):
        self.body.velocity.y = vy

    def setVelZ(self, vz):
        self.body.velocity.z = vz

    def setRadio(self, radio):
        self.body.radius = radio

    def setColor(self, color):
        self.body.color = color

    def addVecina(self,vecinaIndex):
        listaVecinas = self.vecinas
        listaVecinas.append(vecinaIndex)
        self.vecinas = listaVecinas
    
    def getVecinas(self):
        return self.vecinas
    
    def setListaVecinas(self, lista):
        self.vecinas = lista
    
    
    def setFuerza(self,Fij):
        self.fuerzas = Fij
    
    def getFuerzas(self):
        return self.fuerzas
    
    def getEstadoColision(self):
        return self.estadoColision
    
    def cambiaEstadoColision(self):
        estado = self.estadoColision
        nuevoEstado = not(estado)
        self.estadoColision = nuevoEstado
    
    def setEstadoColision(self, estado):
        self.estadoColision = estado
        
