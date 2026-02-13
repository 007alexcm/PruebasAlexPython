# PROGRAMA PRINCIPAL
from Jugador import Jugador
from Portero import Portero
from EquipoFutbol import Equipo

def main():
    print("\nPROYECTO INICIADO")
    alex = Jugador("Alex", 7, False)
    j1 = Portero("Casillas", 1, False)
    j2 = Jugador("Ramos", 4, True)
    j3 = Jugador("Iniesta", 8, False)
    j4 = Jugador("Torres", 9, False)
    j5 = Jugador("Pepe", 2, False)
    print(alex)
    print(j1.nombre)

    mi_equipo = Equipo("España", [alex, j1, j3, j4, j5])
    print("Mi equipo es: ")
    mi_equipo.muestra_equipo()
    mi_equipo.fichar(j2)
    mi_equipo.muestra_equipo()
    print(mi_equipo.solo_porteros().nombre)
    mi_equipo.solo_porteros().muestra_equipo()
    print(mi_equipo.prox_partido().nombre)
    mi_equipo.prox_partido().muestra_equipo()


    print("\n")

if __name__ == "__main__":
    main()
