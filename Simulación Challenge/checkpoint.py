# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def Factorial(numero):

    factorial = 1
    if type(numero) != int or numero <1:
        return None
    for i in range(2, numero+1):
        factorial = factorial * i
    return factorial

def EsPrimo(valor):

    #valor = 1

    if type(valor) != int:
        return None
    elif valor ==2:
        es_primo= True
    else:
        for i in range(2,valor):
            if valor % i == 0:
                es_primo = False
                break
        else:
            es_primo = True

    return es_primo
    
def ClaseAnimal(especie, color):


    class Animal:
        def __init__(self, especie, color):
            self.edad = 0
            self.especie = especie
            self.color = color
        
        def CumplirAnios(self):
            self.edad = self.edad + 1 #(self.edad += 1)
            return self.edad
        
    return Animal(especie,color)
