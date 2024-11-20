"""
Crea un programa en Python que realice los siguiente:
 Escriba el texto “Hola mundo”
 Pida al usuario que introduzca su nombre, almacene el nombre introducido en
una variable y muestre de que tipo es dicha variable (type(nom_variable))
 Pida al usuario que introduzca sus apellidos, almacene los apellidos introducidos
en una variable y muestre de que tipo es dicha variable (type(nom_variable))
 Pida al usuario que introduzca su edad, almacene la edad introducida en una
variable y muestre de que tipo es dicha variable (type(nom_variable))
 Muestre por pantalla sin salida formateada el siguiente mensaje “<apellidos>,
<nombre> tiene <edad> años”, sustituir <apellidos>, <nombre> y <edad> por
los valores introducidos.
 Muestre por pantalla utilizando salida formateada el siguiente mensaje
“<apellidos>, <nombre> tiene <edad> años”, sustituir <apellidos>, <nombre> y
<edad> por los valores introducidos.
"""

print("Hola mundo")
nombre = input("Nombre: ")
print(type(nombre))
apellidos = input("Apellidos: ")
print(type(apellidos))
edad = input("Edad: ")
print(type(edad))

print( apellidos + ", " + nombre +" tiene " + edad + " años.")
print(f"{apellidos}, {nombre} tiene {edad} años")