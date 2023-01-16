from operaciones import Operaciones

class main ():
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
        7) SALIR
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

        elif opcion == 5:
            Operaciones.raiz()

        elif opcion == 6:
            Operaciones.exponente()

        
        elif opcion == 7:
            print("Hasta pronto")
            break
        else:
            print("Opción incorrecta")