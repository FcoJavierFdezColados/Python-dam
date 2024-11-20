from enum import Enum


class Vehiculo:
    __color: str
    __ruedas: int

    def __init__(self, color, ruedas):
        self.__color = color
        self.__ruedas = ruedas

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def ruedas(self):
        return self.__ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        self.__ruedas = ruedas


class Coche(Vehiculo):
    __velocidad: float
    __cilindrada: int

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.__velocidad = velocidad
        self.__cilindrada = cilindrada

    @property
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self.__velocidad = velocidad

    @property
    def cilindrada(self):
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada


class Camioneta(Coche):
    __carga: float

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.__carga = cilindrada

    @property
    def carga(self):
        return self.__carga

    @carga.setter
    def carga(self, carga):
        self.__carga = carga


class Bicicleta(Vehiculo):

    __tipo = Enum(
        value= 'Tipo',
        names=('urbana', 'deportiva')
    )