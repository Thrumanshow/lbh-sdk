"""
LBH SDK v0.2.0
exceptions.py

Jerarquía oficial de excepciones del protocolo
Lenguaje Binario HormigasAIS (LBH)

Autor:
Cristhiam Leonardo Hernández Quiñonez (CLHQ)

Proyecto:
https://github.com/Thrumanshow/lbh-sdk
"""

__version__ = "0.2.0"


class LBHError(Exception):
    """
    Excepción base para todo el SDK LBH.
    """
    pass


class InvalidPacketError(LBHError):
    """
    El paquete LBH recibido no cumple la especificación.
    """
    pass


class InvalidPayloadError(LBHError):
    """
    El payload no pudo ser decodificado o es inválido.
    """
    pass


class InvalidHeaderError(LBHError):
    """
    El HEADER no cumple el formato oficial.
    """
    pass


class InvalidTypeCodeError(LBHError):
    """
    TYPE_CODE desconocido o inválido.
    """
    pass


class InvalidLengthError(LBHError):
    """
    La longitud declarada no coincide con el payload.
    """
    pass


class InvalidHMACError(LBHError):
    """
    La firma HMAC no es válida.
    """
    pass


class UnsupportedVersionError(LBHError):
    """
    La versión del protocolo no es compatible.
    """
    pass


__all__ = [
    "LBHError",
    "InvalidPacketError",
    "InvalidPayloadError",
    "InvalidHeaderError",
    "InvalidTypeCodeError",
    "InvalidLengthError",
    "InvalidHMACError",
    "UnsupportedVersionError",
]
