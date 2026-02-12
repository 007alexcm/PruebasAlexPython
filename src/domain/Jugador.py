# archivo: main.py

class Jugador:
    def __init__(self, nombre: str, dorsal: int, lesion: bool):
        self._nombre = nombre
        self._dorsal = dorsal
        self._lesion = lesion

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, new_name):
        if not new_name.isalpha():
            raise ValueError("El nombre no es válido")
        self._nombre = new_name

    @property
    def dorsal(self):
        return self._dorsal
    
    @property
    def lesion(self):
        return self._lesion
    
    def muestra_nombre(self):
        return self.nombre
    
    def muestra_jug(self):
        return f"Jugador: (nombre={self.nombre!r}, dorsal={self.dorsal}, lesion={self.lesion})"
    
