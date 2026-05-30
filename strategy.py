from abc import ABC, abstractmethod


class EstrategiaDescuento(ABC):

    @abstractmethod
    def calcular(self, precio_base: float) -> float:
        pass


class SinDescuento(EstrategiaDescuento):

    def calcular(self, precio_base):
        return precio_base


class DescuentoPorcentaje(EstrategiaDescuento):

    def __init__(self, porcentaje: float):
        self.porcentaje = porcentaje

    def calcular(self, precio_base):
        return precio_base * (1 - self.porcentaje / 100)


class DescuentoTemporada(EstrategiaDescuento):

    def calcular(self, precio_base):
        return precio_base * 0.70


class CarritoCompra:

    def __init__(self, estrategia: EstrategiaDescuento):
        self.estrategia = estrategia

    def cambiar_estrategia(self, estrategia: EstrategiaDescuento):
        self.estrategia = estrategia

    def precio_final(self, precio_base: float) -> float:
        return self.estrategia.calcular(precio_base)



carrito = CarritoCompra(SinDescuento())

print(carrito.precio_final(100))

carrito.cambiar_estrategia(DescuentoPorcentaje(15))
print(carrito.precio_final(100))

carrito.cambiar_estrategia(DescuentoTemporada())
print(carrito.precio_final(100))