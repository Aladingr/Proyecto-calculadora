from operaciones import Operaciones

def main ():
    opcion = 0
    while True:
        print("""
        CALCULADORA
     
        1) SUMA
        2) RESTA
        3) MULTIPLICACION
        4) DIVIDIR
        5) RAIZ
        6) EXPONENTE
        7) SENO
        8) SALIR
        """)
        opcion = int(input("Elige una opción: ") )     
    

        if opcion == 1:
            print("\n SUMA")
            Operaciones.suma()        
       
        elif opcion == 2:
            print(" ")
            Operaciones.resta()
        elif opcion == 3:
            print(" ")
            Operaciones.multiplicacion()
        
        elif opcion == 4:
            Operaciones.division()
        
        elif opcion == 8:
            print("Hasta pronto")
            break
        else:
            print("Opción incorrecta")