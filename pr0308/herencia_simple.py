from enum import Enum

class Tipo(Enum):
    URBANA = "Urbana",
    DEPORTIVA = 'Deportiva'

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

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        if isinstance(tipo, Tipo):
            self._tipo = tipo
        else:
            raise ValueError("Tipo debe ser una instancia de Tipo Enum")

class Motocicleta(Bicicleta):
    __velocidad: float
    __cilindrada: int

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
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


def catalogar(vehiculos):
    for vehiculo in vehiculos:
        if isinstance(vehiculo, Vehiculo):
            atributos = f"color {vehiculo.color}, ruedas {vehiculo.ruedas}"

        if isinstance(vehiculo, Coche):
            atributos = (f"color {vehiculo.color}, ruedas {vehiculo.ruedas}, "
                         f"velocidad {vehiculo.velocidad} Km/h, cilindrada {vehiculo.cilindrada} cc")

        if isinstance(vehiculo, Camioneta):
            atributos = (f"color {vehiculo.color}, ruedas {vehiculo.ruedas}, velocidad {vehiculo.velocidad}, "
                         f"cilindrada {vehiculo.cilindrada} cc, carga {vehiculo.carga} Kg")

        if isinstance(vehiculo, Bicicleta):
            atributos = f"color {vehiculo.color}, ruedas {vehiculo.ruedas} tipo {(vehiculo.tipo)}"

        if isinstance(vehiculo, Motocicleta):
            atributos = (f"color {vehiculo.color}, ruedas {vehiculo.ruedas} tipo {vehiculo.tipo} "
                         f"velocidad {vehiculo.velocidad} Km/h, cilindrada {vehiculo.cilindrada} cc")

        clase = vehiculo.__class__.__name__

        print(f"{clase} -> {atributos}")



if __name__== '__main__':
    vehiculos = [
        Vehiculo("Rojo", 4),
        Coche("Azul", 4, 200, 2000),
        Camioneta("Verde", 4, 150, 3000),
        Bicicleta("Naranja", 2, Tipo.URBANA.value[0]),
        Motocicleta("Amarillo", 2, Tipo.DEPORTIVA, 300, 1000)
    ]

    catalogar(vehiculos)