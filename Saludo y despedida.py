def saludar():
    print("¡Hola! Bienvenido al menú.")

def despedirse():
    print("¡Hasta luego! Gracias por usar el menú.")

def mostrar_menu():
    print("\n--- Menú Simple ---")
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")
    print("-------------------")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            saludar()
        elif opcion == '2':
            despedirse()
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
main()