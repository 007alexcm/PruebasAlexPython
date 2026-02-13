from Portero import Portero
class Equipo:
    MAX = 3

    def __init__(self, nombre: str, plantilla: list):
        self._nombre = nombre
        self._plantilla = plantilla

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def plantilla(self):
        return self._plantilla
    
    @nombre.setter
    def nombre(self, new_name):
        if not new_name.isalpha():
            raise ValueError("El nombre no es válido")
        self._nombre = new_name
    
    # Funciones
    """
    muestraequipo
    fichar
    fincontrato
    soloporteros
    sinporteros 
    proxpartido """

    def muestra_equipo(self):
        for jug in self.plantilla:
            print(jug.nombre)

    def fichar(self, jug):         # Mejorar buscando primero si el jugador ya existe en plantilla
        self.plantilla.append(jug)

    def fin_contrato(self, jug):    
        self.plantilla.remove(jug)

    """    Esta sería la forma tradicional con for de hacerlo, pero mejor con lambda
    def solo_porteros(self):
        porteros = []
        for jug in self.plantilla:
            if isinstance(jug, Portero):
                porteros.append(jug)
        return Equipo(f"Porteros de {self.nombre}", porteros)
    """

    def solo_porteros(self):
        porteros = list(filter(lambda jug: isinstance(jug, Portero), self.plantilla))
        return Equipo(f"Porteros de {self.nombre}", porteros)

    def prox_partido(self): 
        """ 1. filtrar solo jugadores sanos
            2. ordenar
            3. devuelve como mucho MAX jugadores
        """

        sanos = list(filter(lambda jug: not jug.lesion, self.plantilla))
        sanos.sort(key=lambda jug: jug.dorsal)
        
        return Equipo(f"Alineación de {self.nombre}:", sanos[:Equipo.MAX])
        