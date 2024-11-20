"""
Crea en Python un programa que realice lo siguiente:
o Crea una lista que tenga los siguientes valores: 1, 1, 2, 2, 3
o Mostrar por pantalla el contenido de la lista
o Borrar el primer 1 de la lista y mostrar el resultado
o Borrar la posición 0 de la lista y mostrar el resultado
o Indicar el número de veces que aparece el número 2 en la lista
o Encontrar la primera posición del número 2 en la lista
o Indicar la longitud de la lista
o Añadir al final de la lista el texto “mundo” y mostrar el resultado
o Añadir en la posición 3 el texto hola y mostrar el resultado
o Insertar al final de la lista, la lista 3,2,1 y mostrar el resultado
"""

lista = [1, 1, 2, 2, 3]

print(f"\nMOSTRAR EL CONTENIDO DE LA LISTA:")
print(lista)

print(f"\nBORRAR EL PRIMER 1 DE LAL ISTA Y MOSTRAR EL RESULTADO:")
lista.remove(1)
print(lista)

print(f"\nBORRAR LA POSICION 0 DE LAL LISTA Y MOSTRAR EL RESULTADO:")
lista.pop(0)
print(lista)

print(f"\nINDICAR EL NÚMERO DE VECES QUE APARECE EL 2 EN LA LISTA:")
print(lista.count(2))

print(f"\nINDICAR LA PRIMERA POSICIÓN DEL NÚMERO 2 EN LA LISTA:")
print(lista.index(2))

print(f"\nLONGITUD DE LA LISTA:")
print(len(lista))

print(f"\nAÑADIR AL FINAL DE LA LISTA EL TEXTO mundo Y MOSTRAR LA LISTA:")
lista.append('mundo')
print(lista)

print("\nAÑADIR EN LA POSICIÓN 3 DE LA LISTA EL TEXTO mundo Y MOSTRAR LA LISTA:")
lista.insert(3, 'mundo')
# lista[3] = 'Hola' # Sustituye la posición 3
print(lista)

print("\nINSERTAR AL FINAL DE LA LISTA, LA LISTA 3, 2, 1 Y MOSTRAR EL RESULTADO:")
lista.extend([3, 2, 1])
print(lista)
