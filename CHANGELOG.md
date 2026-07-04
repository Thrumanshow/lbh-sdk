# CHANGELOG

Todas las modificaciones importantes del **LBH SDK** serán registradas en este documento.

El formato está inspirado en **Keep a Changelog** y sigue el versionado semántico.

---

## [0.3.0] - 2026-07-03

### Añadido

- API pública consolidada.
- `encode_packet()`
- `decode_packet()`
- `validate_packet()`
- `generate_hmac()`
- `validate_hmac()`

### Nueva arquitectura

- `constants.py`
- `exceptions.py`

### Calidad

- Suite pública de **16 pruebas automatizadas**.
- Validación de:
  - encode_packet()
  - decode_packet()
  - validate_packet()
  - generate_hmac()
  - validate_hmac()

### Documentación

- README profesional.
- Arquitectura del paquete LBH.
- Tabla oficial TYPE_CODE.
- Compatibilidad de versiones.
- Ejemplos de excepciones.
- Referencias a LBH_SPEC_v2.0.md.

---

## [0.2.0]

### Añadido

- Constantes oficiales del protocolo.
- Jerarquía de excepciones propias del SDK.

---

## [0.1.0]

### Primera versión pública

Incluye:

- encode_packet()
- decode_packet()
- validate_packet()
- generate_hmac()
- validate_hmac()

Primera implementación pública de referencia basada en **LBH_SPEC_v2.0.md**.

---

# Política del CHANGELOG

Este archivo documenta exclusivamente la evolución del **SDK público**.

No registra:

- Infraestructura privada de HormigasAIS.
- Arquitectura interna del nodo A16.
- Motores biológicos.
- Configuración de producción.
- Componentes internos de XOXO.
- Secretos, claves o topologías privadas.

Toda modificación de producción pertenece al ecosistema privado de HormigasAIS y queda fuera del alcance de este repositorio.

---

# Referencias

SDK

https://github.com/Thrumanshow/lbh-sdk

Especificación oficial

https://github.com/Thrumanshow/Lenguaje-Binario-HormigasAIS-

Documento:

LBH_SPEC_v2.0.md
