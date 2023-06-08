# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    factorial = 1
    if type(numero) != int or numero <1:
        return None
    for i in range(2, numero+1):
        factorial = factorial * i
    return factorial

def EsPrimo(valor):
    '''
    Esta función devuelve el valor booleano True si el número reibido como parámetro es primo, de lo 
    contrario devuelve False..
    En caso de que el parámetro no sea de tipo entero debe retornar nulo.
    Recibe un argumento:
        valor: Será el número a evaluar
    Ej:
        EsPrimo(7) debe retornar True
        EsPrimo(8) debe retornar False
    '''
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
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''


    # class Animal:
    #     def __init__(self, especie, color):
    #         self.especie = especie
    #         self.color = color
    #         self.edad= 0

    #     def cumplirAnios(self):
    #         self.edad += 1
    #         return self.edad
    
    # return Animal(especie,color)

    class Animal:
        def __init__(self, especie, color):
            self.edad = 0
            self.especie = especie
            self.color = color
        
        def CumplirAnios(self):
            self.edad = self.edad + 1 #(self.edad += 1)
            return self.edad
        
    return Animal(especie,color)
