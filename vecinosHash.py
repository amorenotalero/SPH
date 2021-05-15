from vpython import *
from particula import *
from sistemaParticulas import *
import math

def calculaVecinosHash(listaParticulas,h):
    n = listaParticulas.getNumParticulas()
    nh = prime(2*n)
    hash_table = {}
    #Anadimos cada particula asociada a su correspondiente clave    
    for p in listaParticulas.getParticulas():
        
        r = p.getPosicion()
        rUnit = rUnitario(r,h)
        key = hash(rUnit,nh)
        if(key in hash_table.keys()):
            hash_table[key].append(p)
        else:
            hash_table[key] = [p]
    #Por cada particula, calculamos sus limites MAX y MIN e iteramos sobre
    #cada posicion discreta, asociando a P las particulas asociadas a esas posiciones
    
    for p in listaParticulas.getParticulas():
        listaVecinas = []      
        rQ = p.getPosicion()
        rUnit = rUnitario(rQ,h) 
        rMin = rQ - vector(h,h,h)
        rMax = rQ + vector(h,h,h)
        #Calculamos los limites
        BBMin = rUnitario(rMin,h)
        BBMax = rUnitario(rMax,h)
        #Iteramos sobre las direcciones entre posMin y posMax
        i = BBMin.x
        j = BBMin.y
        k = BBMin.z
        while i < (BBMax.x+1):
            while j < (BBMax.y+1):
                while k < (BBMax.z+1):
                    key = hash(vector(i,j,k),nh)
                    if(key in hash_table.keys()):
                        for elem in hash_table[key]:
                            if(listaVecinas.count(elem)==0 and elem!=p):#asegura que no esta en la lista de vecinas y que no es la misma particula
                                d = mag(elem.getPosicion()-p.getPosicion())
                                if d < h:
                                    indexParticulaElem = listaParticulas.getIndex(elem)
                                    #listaVecinas.append(indexParticulaElem)
                                    p.addVecina(indexParticulaElem)
                                    indexParticulaP = listaParticulas.getIndex(p)
                                    listaParticulas.changeParticula(indexParticulaP,p)
                                    
                                    

                    k = k + 1
                k = BBMin.z
                j = j + 1
            k = BBMin.z
            j = BBMin.y
            i = i + 1
        #p.setListaVecinas(listaVecinas)#<---adaptar a vuestro proyecto


   
def prime(x):
    i = x
    while(isPrime(i)== False):
        i=i+1
    return i

def isPrime(number):
    if number<=1 or number%2==0:
        return 0
    check=3
    maxneeded=number
    while check<maxneeded+1:
        maxneeded=number/check
        if number%check==0:
            return 0
        check+=2
    return 1

def hash(rUnit,nh):    
    p1 = 73856093
    p2 = 19349663
    p3 = 83492791
    return math.fmod((int(rUnit.x*p1) ^ int(rUnit.y*p2) ^ int(rUnit.z*p3)),nh)

def rUnitario(r,h):
    i = int(math.floor(r.x/h))
    j = int(math.floor(r.y/h))
    k = int(math.floor(r.z/h))
    return vector(i,j,k)
