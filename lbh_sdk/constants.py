"""
LBH SDK v0.2.0
constants.py

Constantes oficiales del protocolo
Lenguaje Binario HormigasAIS (LBH)

Fuente de referencia:
LBH_SPEC_v2.0.md

Autor:
Cristhiam Leonardo Hernández Quiñonez (CLHQ)

Proyecto:
https://github.com/Thrumanshow/lbh-sdk
"""

__version__ = "0.2.0"

# ==========================================================
# TYPE_CODE oficiales
# ==========================================================

TYPE_SEAL = "5345414c"
TYPE_VERI = "56455249"
TYPE_SYNC = "53594e43"
TYPE_PING = "50494e47"
TYPE_FUEL = "4655454c"
TYPE_ACKK = "41434b4b"
TYPE_ERRR = "45525252"

# ==========================================================
# Longitudes oficiales
# ==========================================================

HEADER_LENGTH = 8
TYPE_LENGTH = 8
LENGTH_FIELD = 8
MIN_FRAME_LENGTH = 24

# ==========================================================
# Codificación
# ==========================================================

DEFAULT_ENCODING = "utf-8"

# ==========================================================
# Algoritmo criptográfico
# ==========================================================

DEFAULT_HASH = "sha256"

# ==========================================================
# API pública
# ==========================================================

__all__ = [
    "TYPE_SEAL",
    "TYPE_VERI",
    "TYPE_SYNC",
    "TYPE_PING",
    "TYPE_FUEL",
    "TYPE_ACKK",
    "TYPE_ERRR",
    "HEADER_LENGTH",
    "TYPE_LENGTH",
    "LENGTH_FIELD",
    "MIN_FRAME_LENGTH",
    "DEFAULT_ENCODING",
    "DEFAULT_HASH",
]
