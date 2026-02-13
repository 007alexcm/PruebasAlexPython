import util_texto
from util_texto import validar_basico, colorear
from util_texto import validador
from util_texto.coloreador import resaltar_si

def main():
    print("Metadatos:")
    print(util_texto.__title__)
    print(util_texto.__version__)

    t = "Ana"
    ok, msg = validar_basico(t)
    print("Validación desde paquete:", ok, msg)

    ok2, msg2 = validador.validar_basico("Ana_123")
    print("Validación desde módulo:", ok2, msg2)

    print(colorear("Mensaje coloreado (función reexportada)", "azul"))
    print(resaltar_si("Resaltado condicional", True, "amarillo"))


if __name__ == "__main__":
    main()