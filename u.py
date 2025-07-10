mayor = -1
menor = 101

while True:
    print("***MENÚ PRINCIPAL***")
    print("1. Ingresar número")
    print("2. Mostrar mayor")
    print("3. Mostrar menor")
    print("4. Terminar programa")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        while True:
            try:
                numero = int(input("Ingrese un número entre el 0 y el 100: "))
                if numero >= 0 and numero <= 100:
                    print("Ingreso exitoso")
                    break
                else:
                    print("El número debe ser entre el 0 y el 100")
            except ValueError:
                    print("El número debe ser entero")
        if numero > mayor:
                 mayor = numero
        elif numero < menor:
                 menor = numero
    
    elif opcion == "2":
        if mayor == -1:
            print("No se han registrado números")
        else:
            print("El número mayor registrado hasta el momento es:", mayor)
    
    elif opcion == "3":
        if menor == 101:
            print("No se han registrado números")
        else:
            print("El número menor registrado hasta el momento es:", menor)
        
    elif opcion == "4":
        print("Fin del programa, Adiós")
        break

    else:
        print("Ingrese una opción válida")

        

            

    