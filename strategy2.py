from abc import ABC, abstractmethod


class EstrategiaOrdenacion(ABC):

    @abstractmethod
    def ordenar(self, datos: list) -> list:
        pass


class OrdenacionBurbuja(EstrategiaOrdenacion):

    def ordenar(self, datos):
        d = datos[:]
        n = len(d)

        for i in range(n):
            for j in range(0, n - i - 1):
                if d[j] > d[j + 1]:
                    d[j], d[j + 1] = d[j + 1], d[j]

        return d


class OrdenacionRapida(EstrategiaOrdenacion):

    def ordenar(self, datos):

        if len(datos) <= 1:
            return datos

        pivot = datos[len(datos) // 2]

        izq = [x for x in datos if x < pivot]
        med = [x for x in datos if x == pivot]
        der = [x for x in datos if x > pivot]

        return self.ordenar(izq) + med + self.ordenar(der)


class Ordenador:

    def __init__(self, estrategia: EstrategiaOrdenacion):
        self.estrategia = estrategia

    def ejecutar(self, datos: list) -> list:
        return self.estrategia.ordenar(datos)



datos = [5, 2, 8, 1, 9, 3]

ordenador = Ordenador(OrdenacionBurbuja())
print(ordenador.ejecutar(datos))

ordenador.estrategia = OrdenacionRapida()
print(ordenador.ejecutar(datos))