import threading


class PoolConexiones:
    _instancia = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instancia is None:
                cls._instancia = super().__new__(cls)
                cls._instancia._conexiones = []
                cls._instancia._max = 5
                print("[Pool] Inicializando pool de conexiones...")

        return cls._instancia

    def obtener_conexion(self):
        if len(self._conexiones) < self._max:
            conn = f"Conexion-{len(self._conexiones)+1}"
            self._conexiones.append(conn)
            return conn

        return "Sin conexiones disponibles"

    def estado(self):
        return f"{len(self._conexiones)}/{self._max} conexiones activas"



pool_a = PoolConexiones()
pool_b = PoolConexiones()

print(pool_a is pool_b)

print(pool_a.obtener_conexion())
print(pool_b.estado())