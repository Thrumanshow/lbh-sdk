"""
LBH SDK v0.2.0
=================================

Referencia oficial del protocolo
Lenguaje Binario HormigasAIS (LBH)

Implementación pública basada en:

- LBH_SPEC_v2.0.md

Autor:
Cristhiam Leonardo Hernández Quiñonez (CLHQ)

Proyecto:
https://github.com/Thrumanshow/lbh-sdk
"""

from __future__ import annotations

import hashlib
import hmac

from .exceptions import (
    InvalidPacketError,
    InvalidPayloadError,
)

__version__ = "0.2.0"


def encode_packet(header: str, type_code: str, payload: str) -> str:
    payload_hex = payload.encode("utf-8").hex()
    length = format(len(payload.encode("utf-8")), "08x")
    return f"{header}{type_code}{length}{payload_hex}"


def decode_packet(frame: str) -> dict:

    if len(frame) < 24:
        raise InvalidPacketError(
            "Frame LBH demasiado corto."
        )

    try:

        header = frame[:8]
        type_code = frame[8:16]
        length = int(frame[16:24], 16)

        payload_hex = frame[24:]
        payload = bytes.fromhex(payload_hex).decode("utf-8")

    except UnicodeDecodeError as e:
        raise InvalidPayloadError(str(e))

    except ValueError as e:
        raise InvalidPacketError(str(e))

    return {
        "header": header,
        "type_code": type_code,
        "length": length,
        "payload": payload,
    }


def validate_packet(frame: str) -> bool:

    try:
        packet = decode_packet(frame)
        return packet["length"] == len(packet["payload"].encode("utf-8"))

    except (InvalidPacketError, InvalidPayloadError):
        return False


def generate_hmac(message: str, secret_key: str) -> str:

    return hmac.new(
        secret_key.encode("utf-8"),
        message.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()


def validate_hmac(message: str,
                  secret_key: str,
                  received_hmac: str) -> bool:

    expected = generate_hmac(message, secret_key)

    return hmac.compare_digest(expected, received_hmac)


__all__ = [
    "encode_packet",
    "decode_packet",
    "validate_packet",
    "generate_hmac",
    "validate_hmac",
]
