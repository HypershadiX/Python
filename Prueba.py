condition1 = False
condition2 = False
condition3 = False
condition4 = False
condition5 = False
condition6 = False

while True:
 contrasenia = input("Ingrese la contraseña: ")
 if len(contrasenia) >= 8 and len(contrasenia) <= 16:
      condition1 = True

 for i in contrasenia:
   if i in '1234567890':
      condition2 = True

   if i in 'qwertyuiopasdfghjklñzxcvbnm':
       condition3 = True

   if i in '-_*.!?#$%':
       condition4 = True

   if ' ' not in i:
       condition5 = True
   
   if contrasenia[-1] not in '-_*.!?#$%':
       condition6 = True

 if condition1 and condition2 and condition3 and condition4 and condition5 and condition6:
       print("Contraseña válida")
       break
   
 else:
   if condition1 == False:
       print("El largo de la contraseña debe ser de mínimo 8 caracteres y máximo 16")

   if condition2 == False:
       print("La contraseña debe tener al menos 1 número")

   if condition3 == False:
       print("La contraseña debe tener mínimo una letra, ya sea minúscula o mayúscula")

   if condition4 == False:
       print("La contraseña debe tener como máximo 1 carácter especial")

   if condition5 == False:
       print("La contraseña no puede tener espacios en blanco")

   if condition6 == False:
       print("La contraseña no puede terminar con un carácter especial")
   print("Intente nuevamente")
    