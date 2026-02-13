# util_texto/coloreador.py

# Códigos ANSI simples para terminal

_RESET = "\033[0m"

_COLORES = {
    "rojo": "\033[31m",
    "verde": "\033[32m",
    "amarillo": "\033[33m",
    "azul": "\033[34m",
}

def colorear(texto: str, color: str) -> str:

    """Devuelve texto envuelto en un color ANSI (si existe)."""

    pref = _COLORES.get(color.lower())
    if pref is None:

        return texto  # si no existe color, no cambia nada
    return f"{pref}{texto}{_RESET}"

def resaltar_si(texto: str, condicion: bool, color: str = "amarillo") -> str:
    """Colorea texto solo si condicion es True."""
    return colorear(texto, color) if condicion else texto

def main():

    print(colorear("Hola", "verde"))
    print(colorear("Error", "rojo"))
    print(resaltar_si("Esto se resalta", True, "azul"))
    print(resaltar_si("Esto no", False, "azul"))


if __name__ == "__main__":
    main()