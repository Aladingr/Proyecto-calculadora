import math as mt

class Operaciones:
    a = 0
    b = 0
    resultado = 0

    def suma ():
        a = float(input("Ingresa un numero: "))
        #print= ("ingresa un 2 numero: ")
        b = float(input("Ingresa un numero: "))
        resultado = a+b
        print("El Resultado es: ",resultado)

    def resta ():
        #print= ("Ingresa un numero: ")
        a = float(input("Ingresa un numero: "))
        #print= ("ingresa un 2 numero: ")
        b = float(input("Ingresa un numero: "))
        resultado = a-b
        print("El Resultado es: ",resultado)

    def multiplicacion():
        a = float(input("Ingresa un numero: "))
        #print= ("ingresa un 2 numero: ")
        b = float(input("Ingresa un numero: "))
        resultado = a*b
        print("El Resultado es: ",resultado)

    def division():
        a = float(input("Ingresa un numero: "))
        #print= ("ingresa un 2 numero: ")
        b = float(input("Ingresa un numero: "))
        resultado = a*b
        print("El Resultado es: ",resultado)
    
    def raiz():
        a = float(input("Ingresa un numero: "))
        #print= ("ingresa un 2 numero: ")
        b = float(input("Ingresa el numero de raiz que deseas obtener: "))
        resultado = mt.pow(a, 1/b)
        print("El Resultado es: ",resultado)

    def exponente():
        a = float(input("Ingresa numero: "))
        #print= ("ingresa un 2 numero: ")
        b = float(input("Ingresa el exponente al que quieres elevar el numero: "))
        resultado = mt.pow(a, b)
        print("El resultado es: ", resultado)
    
