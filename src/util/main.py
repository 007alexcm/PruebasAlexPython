# main.py

from util_texto import validar_basico, colorear

def main():
    texto = input("Escribe un texto: ")
    ok, msg = validar_basico(texto)
    if ok:
        print(colorear("Texto válido", "verde"))
    else:
        print(colorear(f"Texto inválido: {msg}", "rojo"))

if __name__ == "__main__":
    main()
