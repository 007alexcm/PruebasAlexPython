# archivo: main.py

class Jugador:
    contador_jugadores = 0

    #Constructor
    def __init__(self, nombre: str, dorsal: int, lesion: bool):
        self._nombre = nombre
        self._dorsal = dorsal
        self._lesion = lesion
        Jugador.contador_jugadores += 1

    def __str__(self):
        return f"Jugador: {self.nombre}, dorsal = {self.dorsal}, lesion = {self.lesion}"
    
    @staticmethod
    def jugadores_registrados():
        return Jugador.contador_jugadores
    
    def __eq__(self, otro):
        if isinstance(otro, Jugador):
            return self.nombre == otro.nombre
        return False
    
    #Getter y setter
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
    
    @dorsal.setter
    def dorsal(self, valor):
        if not valor.isnum():
            print("Dorsal no válido")
        self._dorsal = valor
    
    @property
    def lesion(self):
        return self._lesion
    
    @lesion.setter
    def lesion(self, valor):
        self._lesion = valor
    

    
    
