"""
Modifica el programa Python de funciones para que:
o Todas las funciones deben capturar las excepciones:
▪ TyperError por si se está intentando realizar la operación por valores no
numéricos
▪ Cualquier otro tipo de excepción que se pueda producir
o La función división debe capturar si se intenta dividir entre 0.
o Las excepciones capturadas deben ser lanzadas hacia arriba y capturadas en el
main mostrando el mensaje correspondiente. Asimismo, se deberá capturar la
excepción que podría suceder si el usuario introduce un valor no numérico.
"""
from pyexpat.errors import messages


def suma(a: int, b: int) -> int:
    return a + b


def resta(a: int, b: int) -> int:
    return a - b


def multiplicacion(a: int, b: int) -> int:
    return a * b


def division(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir por zero")


if __name__ == "__main__":
    try:
        numberA = int(input("Introduce el número A:"))
        numberB = int(input("Introduce el número B:"))
    except ValueError:
        print("El tipo de dato introducido no es numérico")
    except Exception as e:
        print(f"Error: {repr(e)}")

    try:
        print(suma(numberA, numberB))
        print(resta(numberA, numberB))
        print(multiplicacion(numberA, numberB))
        print(division(numberA, numberB))
    except NameError as ex:
        print(f"{str(ex)}")
    except Exception as e:
        print(f"Error: {repr(e)}")