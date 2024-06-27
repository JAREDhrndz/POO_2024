from clases import Rectangulo, Circulo, Triangulo

rectangulo = Rectangulo(4.0, 6.0)
print(f"Área del rectangulo: {rectangulo.calcular_area()}")

circulo = Circulo(5.0)
print(f"Área del circulo: {circulo.calcular_area()}")

triangulo = Triangulo(3.0, 4.0)
print(f"Área del triángulo: {triangulo.calcular_area()}")
