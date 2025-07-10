import random
import sys

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
suma = dado1 + dado2

intento1 = int(input("Primer intento para adivinar el número: "))

if 2 > intento1 or 12 < intento1:
    sys.exit(print("Error, la suma de los dados debe estar dentro del rango"))

elif intento1 != suma:
    print("Primer intento fallido, tienes un segundo intento")

elif intento1 == suma:
    sys.exit(print("¡Adivinaste la suma!"))

if suma % 2 == 0:
    print("Pista: El número es par")

else:
    print ("El número es impar")

intento2 = int(input("Segundo intento para adivinar el número: "))

if 2 > intento2 or 12 < intento2:
    sys.exit(print("Error, la suma de los dados debe estar dentro del rango"))

elif intento2 == suma:
    sys.exit(print("¡Adivinaste la suma!"))

elif intento1 != suma:
    print("No adivinaste la suma secreta")
    print(f"La suma secreta era: {suma}")
          
    








