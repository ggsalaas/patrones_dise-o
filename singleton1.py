class ConfiguracionApp:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._configuracion = {}
            print("[Singleton] Primera instancia creada.")
        else:
            print("[Singleton] Instancia ya existente, devolviendo la misma.")

        return cls._instancia

    def establecer(self, clave, valor):
        self._configuracion[clave] = valor

    def obtener(self, clave):
        return self._configuracion.get(clave, None)



cfg1 = ConfiguracionApp()
cfg1.establecer("tema", "oscuro")
cfg1.establecer("idioma", "es")

cfg2 = ConfiguracionApp()

print(cfg2.obtener("tema"))
print(cfg1 is cfg2)