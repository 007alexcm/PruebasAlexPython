# PROGRAMA PRINCIPAL
import json
from Jugador import Jugador
from Portero import Portero
from EquipoFutbol import Equipo


def main():

    # Para transformar lista de jugadores en json
    def equipo2json(jugadores, nombre_archivo):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(
                [j.to_dict() for j in jugadores],
                archivo,
                indent=4, #esto es el identado que tendrá el json, para hacerlo legible, NO obligatorio
             ensure_ascii=False
            )

    # Para pedir jugador nuevo por terminal
    def pedir_jugador():
        while True:
            try:
                nombre = input("Nombre del jugador: ")
                dorsal = int(input("Dorsal: "))
                lesion = input("Está lesionado (s/n): ").lower() != "n"     #mejorable a más respuestas
                return Jugador(nombre, dorsal, lesion)
            except ValueError as e:
                print(f"Input error: {e}")

    print("\nPROYECTO INICIADO\n")
    #alex = Jugador("Alex", 7, False)
    j1 = Portero("Casillas", 1, False)
    j2 = Jugador("Ramos", 4, True)
    j3 = Jugador("Iniesta", 8, False)
    j4 = Jugador("Torres", 9, False)
    j5 = Jugador("Carvajal", 2, False)
   
    mi_equipo = Equipo("España", [j1, j2, j3, j5])
    print("Nuestro equipo nacional de España está compuesto por: ")
    mi_equipo.muestra_equipo()

    nuevo_jug = pedir_jugador()
    mi_equipo.fichar(nuevo_jug)
    print("\nBienvenido al equipo " + nuevo_jug.nombre)
    
    print(f"\nCONVOCATORIA PRÓXIMO PARTIDO de {mi_equipo.prox_partido().nombre}:")
    mi_equipo.prox_partido().muestra_equipo()
    mi_equipo.prox_partido().felicitacion_disculpa(nuevo_jug)

    equipo2json(mi_equipo.prox_partido().plantilla, "prox_partido.json")
    
    
if __name__ == "__main__":
    main()
