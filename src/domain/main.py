# PROGRAMA PRINCIPAL
from Jugador import Jugador
from Portero import Portero

def main():
    print("Proyecto iniciado\n")
    alex = Jugador("alex", 7, False)
    j1 = Portero("Casillas", 1, False)
    print(alex.muestra_jug)
    print(alex.muestra_nombre)
    alex.muestra_jug
    print(alex.nombre, alex.dorsal, alex.lesion)
    print(j1.nombre, j1.dorsal, j1.lesion)

    print("\n")

if __name__ == "__main__":
    main()
