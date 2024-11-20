"""
Crea en Python un programa que realice lo siguiente:
o Crea un diccionario que tenga los siguientes valores:
▪ Clave: 1, Valor: valor 1
▪ Clave: 2, Valor: valor 2
▪ Clave: 3, Valor: valor 3
o Mostrar por pantalla el contenido del diccionario
o Mostrar las claves del diccionario
o Mostrar los valores del diccionario
o Mostrar los elementos del diccionario
o Mostrar el valor del diccionario que corresponda a la clave 1
o Añadir un elemento al diccionario con:
▪ Clave: 4, Valor: valor 4
o Borrar del diccionario el elemento con clave 1
"""

diccionario = {1: "valor 1", 2: "valor 2", 3: "valor 3"}
print("MOSTRAR POR PANTALLA EL VALOR DEL DICCIONARIO:")
print(diccionario)

print("\nMOSTRAR LAS CLAVES DEL DICCIONARIO:")
print(diccionario.keys())

print("\nMOSTRAR LOS VALORES DEL DICCIONARIO:")
print(diccionario.values())

print("\nMOSTRAR LOS ELEMENTOS DEL DICCIONARIO:")
print(diccionario.items())

print("\nMOSTRAR EL VALOR DEL DICCIONARIO QUE CORRESPONDA A LA CLAVE 1:")
print(diccionario.get(1))
print(diccionario[1])

print("\nAÑADIR AL DICCIONARIO LA CLAVE 4 CON EL VALOR DE 'clave 4'")
diccionario[4] = "valor 4"
print(diccionario)

print("\nBORRAR DEL DICCIONARIO EL ELEMENTO CON CLAVE 1")
del(diccionario[1])
print(diccionario)