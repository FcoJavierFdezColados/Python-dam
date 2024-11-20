"""
Sistemas de Gestión Empresarial Tema 3-Prácticas
Desarrollo de Aplicaciones Multiplataforma Introducción a Python
Tuplas
• Crea en Python un programa que realice lo siguiente:
o Crea una tupla que tenga los siguientes valores: 1, 2, hola, 2, mundo
o Muestra por pantalla el contenido de la tupla
o Muestra la suma de los valores de las posiciones 0, 1 y 3
o Concatena las posiciones 2 y 4 y muestra el resultado por pantalla
o Muestra el número de veces que se encuentra el número 2 en la tupla
o Encuentra la primera posición de la palabra “mundo” en la tupla
"""
tupla = (1, 2, "hola", 2, 'mundo')

print("Mostrar el contenido de la tupla:")
print(tupla)

print("\nSumar los valores de las posiciones 0, 1 y 3:")
print(f"{tupla[0] + tupla[1] + tupla[3]}")

print("\nConcatenar los valores de las posiciones 2 y 4:")
print(f"{tupla[2]} {tupla[4]}")

print(f"\nContar el número de veces que se encuentra el número 2 en la tupla:")
print(f"El número 2 está {tupla.count(2)} veces")

print(f'\nEncontrar la primera posición de la palabra "mundo" en la tupla:')
print(tupla.index("mundo"))


