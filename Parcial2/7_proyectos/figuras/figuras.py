from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def CalcularArea(self) -> float:
        pass

class Rectangulo(Figura):
    def _init_(self, largo: float, ancho: float):
        self._largo = largo
        self._ancho = ancho

    @property
    def Largo(self) -> float:
        return self._largo

    @Largo.setter
    def Largo(self, largo: float):
        self._largo = largo

    @property
    def Ancho(self) -> float:
        return self._ancho

    @Ancho.setter
    def Ancho(self, ancho: float):
        self._ancho = ancho

    def CalcularArea(self) -> float:
        return self._largo * self._ancho

class Circulo(Figura):
    def _init_(self, radio: float):
        self._radio = radio

    @property
    def Radio(self) -> float:
        return self._radio

    @Radio.setter
    def Radio(self, radio: float):
        self._radio = radio

    def CalcularArea(self) -> float:
        import math
        return math.pi * (self._radio ** 2)

class Triangulo(Figura):
    def _init_(self, altura: float, ancho: float):
        self._altura = altura
        self._ancho = ancho

    @property
    def Altura(self) -> float:
        return self._altura

    @Altura.setter
    def Altura(self, altura: float):
        self._altura = altura

    @property
    def Ancho(self) -> float:
        return self._ancho

    @Ancho.setter
    def Ancho(self, ancho: float):
        self._ancho = ancho

    def CalcularArea(self) -> float:
        return (self._altura * self._ancho) / 2