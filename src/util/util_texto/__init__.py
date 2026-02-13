# util_texto/__init__.py

"""Paquete de utilidades para validar y colorear texto."""

__title__ = "util_texto"
__version__ = "0.1.0"
__author__ = "Alex"

# Reexportaciones: facilitan importar desde el paquete
from .validador import validar_basico
from .coloreador import colorear

# API pública (opcional pero útil para enseñar intención)
__all__ = ["validar_basico", "colorear", "__version__"]
