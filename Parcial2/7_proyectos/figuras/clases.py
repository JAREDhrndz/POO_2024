from abc import ABC, abstractmethod
import math

# Figura ---------------
class Figura(ABC):
    @abstractmethod
    def calcular_area(self) -> float:
        pass

# Rectangulo -----------
class Rectangulo(Figura):
    def __init__(self, largo: float, ancho: float):
        self._largo = largo
        self._ancho = ancho

    @property
    def largo(self) -> float:
        return self._largo

    @largo.setter
    def largo(self, largo: float):
        self._largo = largo

    @property
    def ancho(self) -> float:
        return self._ancho

    @ancho.setter
    def ancho(self, ancho: float):
        self._ancho = ancho

    def calcular_area(self) -> float:
        return self._largo * self._ancho

# Circulo --------------
class Circulo(Figura):
    def __init__(self, radio: float):
        self._radio = radio

    @property
    def radio(self) -> float:
        return self._radio

    @radio.setter
    def radio(self, radio: float):
        self._radio = radio

    def calcular_area(self) -> float:
        return math.pi * (self._radio ** 2)

# Triangulo --------------
class Triangulo(Figura):
    def __init__(self, altura: float, ancho: float):
        self._altura = altura
        self._ancho = ancho

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, altura: float):
        self._altura = altura

    @property
    def ancho(self) -> float:
        return self._ancho

    @ancho.setter
    def ancho(self, ancho: float):
        self._ancho = ancho

    def calcular_area(self) -> float:
        return (self._altura * self._ancho) / 2
