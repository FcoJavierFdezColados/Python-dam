"""
Crea un programa en Python que realice los siguientes pasos:
o Crea una variable, con el nombre numEntero, que almacene el número 5
o Crea una variable, con el nombre numFloat, que almacene el número 1.25
o Muestra por pantalla el tipo de variables que son
o Escribe por pantalla el valor de las dos variables
o Muestra por pantalla la suma, resta, multiplicación y división de ambas variables
o Muestra por pantalla el resultado de dividir numEntero entre dos y el resto de
dicha operación.
o Muestra por pantalla el valor de numEntero elevado a potencia 3
o Convierte numEntero a float, muestra por pantalla el tipo de variable y su valor
o Convierte numFloat a int y muestra por pantalla el tipo de variable y su valor
"""

numEntero = 5
numFloat = 1.25

print("TIPO DE LAS VARIABLES")
print(type(numEntero))
print(type(numFloat))
print("\n\n")

print("VALOR DE LAS VARIABLES")
print(f"numEntero = {numEntero}")
print(f"numFloat = {numFloat}")
print("\n\n")

print("OPERACIONES BÁSICAS CON LAS VARIABLES")
print(f"numEntero + numFloat = {numEntero + numFloat}")
print(f"numEntero - numFloat = {numEntero - numFloat}")
print(f"numEntero * numFloat = {numEntero * numFloat}")
print(f"numEntero / numFloat = {numEntero / numFloat}")
print(f"numEntero % numFloat = {numEntero % numFloat}")
print("\n\n")


print("DIVISION Y RESTO")
print(numEntero / 2)
print(numEntero % 2)
print("\n\n")

print("POTENCIA")
print(numEntero ** 3)
print("\n\n")

print("CONVERSIÓN DE TIPOS")
numEntero = float(numEntero)
numFloat = int(numFloat)
print(type(numEntero))
print(numEntero)
print(type(numFloat))
print(numFloat)
