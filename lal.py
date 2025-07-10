# Variables de usuario y contraseña
usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None

def registrar_usuario():
    global usuario1, usuario2, usuario3, contrasena1, contrasena2, contrasena3
    try:
        nuevo_usuario = input("Ingrese nuevo usuario: ")
        nueva_contrasena = input("Ingrese nueva contraseña: ")
        
        if usuario1 is None:
            usuario1, contrasena1 = nuevo_usuario, nueva_contrasena
        elif usuario2 is None:
            usuario2, contrasena2 = nuevo_usuario, nueva_contrasena
        elif usuario3 is None:
            usuario3, contrasena3 = nuevo_usuario, nueva_contrasena
        else:
            print("No se pueden registrar más usuarios.")
    except Exception as e:
        print(f"Error en el registro: {e}")

def iniciar_sesion():
    try:
        if usuario1 is None and usuario2 is None and usuario3 is None:
            print("Es necesario registrar un usuario antes de iniciar sesión.")
            return False
        
        usuario = input("Ingrese su usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        if (usuario == usuario1 and contrasena == contrasena1) or \
           (usuario == usuario2 and contrasena == contrasena2) or \
           (usuario == usuario3 and contrasena == contrasena3):
            print("Inicio de sesión exitoso.")
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            return False
    except Exception as e:
        print(f"Error en el inicio de sesión: {e}")
        return False

def realizar_llamada():
    try:
        numero = input("Ingrese el número de celular (debe comenzar con 9 y tener 8 dígitos): ")
        if numero.startswith("9") and len(numero) == 8 and numero.isdigit():
            print(f"Llamando al número {numero}...")
        else:
            print("Número inválido, debe comenzar con 9 y tener exactamente 8 dígitos.")
    except Exception as e:
        print(f"Error al realizar la llamada: {e}")

def enviar_correo():
    try:
        correo = input("Ingrese su correo electrónico: ")
        mensaje = input("Ingrese el mensaje a enviar: ")

        if "@" in correo:
            print(f"Correo enviado a {correo}: {mensaje}")
        else:
            print("Correo inválido, debe contener '@'.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

def menu_principal():
    while True:
        try:
            print("\nMenú principal:")
            print("1) Iniciar sesión")
            print("2) Registrar usuario")
            print("3) Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                if iniciar_sesion():
                    while True:
                        print("\nMenú de usuario:")
                        print("1) Realizar llamada")
                        print("2) Enviar correo electrónico")
                        print("3) Cerrar sesión")
                        opcion_usuario = input("Seleccione una opción: ")

                        if opcion_usuario == "1":
                            realizar_llamada()
                        elif opcion_usuario == "2":
                            enviar_correo()
                        elif opcion_usuario == "3":
                            print("Cerrando sesión...")
                            break
                        else:
                            print("Opción inválida. Intente nuevamente.")
            elif opcion == "2":
                registrar_usuario()
            elif opcion == "3":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except Exception as e:
            print(f"Error en el menú principal: {e}")

# Ejecutar el menú principal
menu_principal()
