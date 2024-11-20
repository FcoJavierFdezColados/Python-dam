class Rectangulo:

    __base: float
    __altura: float

    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def __calcular_area(self, base, altura):
        return base * altura

    def __calcular_perimetro(self, base, altura):
        return 2 * (base + altura)

    def __str__(self):
        return (f"Base = {self.__base}\n"
                f"Altura = {self.__altura}\n"
                f"Area = {self.__calcular_area(self.__base, self.__altura)}\n"
                f"Perimetro = {self.__calcular_perimetro(self.__base, self.__altura)}")
