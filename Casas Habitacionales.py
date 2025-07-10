sueldo = int(input("Ingrese el sueldo: "))
quintil = int(input("Ingrese la cantidad de quintiles: "))
integrantes = int(input("Ingrese la cantidad de integrantes: "))
vivienda = int(input("Ingrese el precio de la vivienda a la que quiere acceder: "))

if (sueldo < 500000) and (quintil == 1 or quintil == 2):
    print("Tiene un subsidio del 15%")
    subsidio = vivienda * 0.15

elif (sueldo < 500000) and (quintil == 3 or quintil == 4):
    print("Tiene un subsidio del 13%")
    subsidio = vivienda * 0.13

elif (sueldo >= 500000 or sueldo <= 700000) and (quintil == 1 or quintil == 2):
    print("Tiene un subsidio del 10%")
    subsidio = vivienda * 0.10

elif (sueldo >= 500000 or sueldo <= 700000) and (quintil == 3 or quintil == 4):
    print("Tiene un subsidio del 5%")
    subsidio = vivienda * 0.05

else:
    print("No tiene subsidio")
    subsidio = vivienda * 0

if integrantes == 3 or integrantes == 4 or integrantes == 5:
    print("Tiene un descuento del 10%")
    descuento = vivienda * 0.10

elif integrantes > 5:
    print("Tiene un descuento del 15%")
    descuento = vivienda * 0.15

else: 
    print("No tiene descuento")
    descuento = vivienda * 0

valor_subsidio = vivienda - subsidio
valor_descuento = vivienda - descuento
subsidio_vivienda = vivienda - valor_subsidio
descuento_vivienda = vivienda - valor_descuento
total = vivienda - subsidio_vivienda - descuento_vivienda

print(f"Resumen de cálculos")

print(f"Sueldo: {sueldo}")
print(f"Quintil: {quintil}")
print(f"Integrantes: {integrantes}")
print(f"Valor casa: {vivienda}")
print(F"Precio total de la casa contando el subsidio y el descuento: {total:.0f}")









