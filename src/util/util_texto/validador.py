# util_texto/validador.py

def es_no_vacio(texto: str) -> bool:

    """Devuelve True si texto tiene al menos un carácter no blanco."""

    return len(texto.strip()) > 0

def longitud_entre(texto: str, minimo: int, maximo: int) -> bool:

    """True si la longitud de texto está entre [minimo, maximo]."""

    n = len(texto)

    return minimo <= n <= maximo

def solo_letras_y_espacios(texto: str) -> bool:

    """True si el texto contiene solo letras (a-z, A-Z) y espacios."""

    # Sencillo y guiado: sin expresiones regulares

    for ch in texto:

        if ch != " " and not ch.isalpha():

            return False

    return True

def validar_basico(texto: str) -> tuple[bool, str]:

    """Valida con reglas básicas y devuelve (ok, mensaje)."""

    if not es_no_vacio(texto):

        return False, "El texto está vacío."

    if not longitud_entre(texto, 3, 30):

        return False, "El texto debe tener entre 3 y 30 caracteres."

    if not solo_letras_y_espacios(texto):

        return False, "Solo se permiten letras y espacios."

    return True, "OK"

def main():

    # Pequeña demo para ver el efecto de __name__

    ejemplos = ["", "  ", "Ana", "Ana_123", "Un nombre válido"]

    for t in ejemplos:

        ok, msg = validar_basico(t)

        print(f"{t!r} -> ok={ok}, msg={msg}")


if __name__ == "__main__":

    # Esto solo se ejecuta si ejecutas ESTE archivo directamente

    main()
