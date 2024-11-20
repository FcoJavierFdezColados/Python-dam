"""
Crea en Python un programa que realice lo siguiente:
o Crear una función suma, recibe dos valores y devuelve la suma
o Crear una función resta, recibe dos valores y devuelve la resta
o Crear una función multiplicación, recibe dos valores y devuelve la multiplicación
o Crear una función división, recibe dos valores y devuelve la división. Debe
comprobar si el divisor es 0, en ese caso devolverá un mensaje de error
o Crear la función main: pide al usuario que introduzca dos números y llama a las
funciones creadas en los puntos anteriores y muestra el resultado
"""


def suma(a: int, b: int) -> int:
    return a + b


def resta(a: int, b: int) -> int:
    return a - b


def multiplicacion(a: int, b: int) -> int:
    return a * b


def division(a: int, b: int) -> float:
    if b == 0:
        print("No se puede dividir por zero")
    else:
        return a / b


if __name__ == "__main__":
    numberA = int(input("Introduce el número A:"))
    numberB = int(input("Introduce el número B:"))

    print(suma(numberA, numberB))
    print(resta(numberA, numberB))
    print(multiplicacion(numberA, numberB))
    print(division(numberA, numberB))
