# LBH SDK

![Version](https://img.shields.io/badge/version-v0.3.0-blue)
![Status](https://img.shields.io/badge/status-stable-green)
![License](https://img.shields.io/badge/license-MPL--2.0-orange)
![Python](https://img.shields.io/badge/python-3.x-blue)
![Tests](https://img.shields.io/badge/tests-16%20passing-brightgreen)

SDK oficial de referencia del protocolo **LBH (Lenguaje Binario HormigasAIS)**.

Implementación pública basada en la especificación **LBH_SPEC_v2.0.md**.

---

# Filosofía del proyecto

LBH SDK nace con un objetivo muy claro:

Construir una implementación pública, ligera, estable y reutilizable del protocolo LBH para facilitar la interoperabilidad entre desarrolladores sin exponer la infraestructura crítica de HormigasAIS.

El SDK representa la capa pública del ecosistema.

La infraestructura de producción (Nodo Maestro A16, agentes propietarios, gobernanza, motores internos y demás componentes estratégicos) permanece completamente separada y bajo control exclusivo de HormigasAIS.

---

# Características

- Codificación de paquetes LBH
- Decodificación de paquetes LBH
- Validación de integridad
- Firma HMAC-SHA256
- Verificación HMAC
- API pública estable
- Suite de pruebas automatizadas (16 tests)

---

# Arquitectura del paquete LBH

Todo paquete LBH sigue la siguiente estructura:

```text
HEADER (8) | TYPE_CODE (8) | LENGTH (8) | PAYLOAD (N)
```

```text
┌─────────────┬─────────────┬─────────────┬────────────────────────┐
│ HEADER      │ TYPE_CODE   │ LENGTH      │ PAYLOAD                │
│ 8 hex       │ 8 hex       │ 8 hex       │ UTF-8 → HEX            │
└─────────────┴─────────────┴─────────────┴────────────────────────┘
```

---

# TYPE_CODE oficiales

| TYPE_CODE | Nombre | Descripción |
|-----------|---------|-------------|
| 5345414C | SEAL | Emisión de sello |
| 56455249 | VERI | Verificación |
| 53594E43 | SYNC | Sincronización |
| 50494E47 | PING | Health Check |
| 4655454C | FUEL | Feromona |
| 41434B4B | ACKK | Confirmación |
| 45525252 | ERRR | Error |

---

# Instalación

```python
import lbh_sdk
```

No requiere dependencias externas.

Compatible con Python 3.

---

# Ejemplo rápido

```python
import lbh_sdk

frame = lbh_sdk.encode_packet(
    "41313600",
    "5345414C",
    "Hola LBH"
)

decoded = lbh_sdk.decode_packet(frame)

print(decoded)
```

---

# Validación

```python
lbh_sdk.validate_packet(frame)
```

Resultado esperado:

```python
True
```

---

# HMAC

```python
digest = lbh_sdk.generate_hmac(
    "Hola LBH",
    "HormigasAIS"
)

ok = lbh_sdk.validate_hmac(
    "Hola LBH",
    "HormigasAIS",
    digest
)
```

---

# Manejo de excepciones

```python
from exceptions import InvalidPacketError

try:
    packet = lbh_sdk.decode_packet(frame)

except InvalidPacketError as e:
    print(e)
```

---

# Casos de uso

LBH SDK puede utilizarse para:

- Comunicación entre agentes inteligentes.
- Automatización distribuida.
- Edge Computing.
- Sistemas IoT.
- Integración entre microservicios.
- Protocolos Machine-to-Machine (M2M).
- Automatización industrial.
- Investigación sobre protocolos binarios.
- Desarrollo de herramientas compatibles con el protocolo LBH.

---

# Compatibilidad

| SDK | Especificación |
|------|----------------|
| v0.3.x | LBH_SPEC_v2.0 |

---

# Cómo contribuir

Las contribuciones son bienvenidas.

Puedes colaborar mediante:

- Reportar errores.
- Abrir Issues.
- Enviar Pull Requests.
- Mejorar la documentación.
- Crear ejemplos.
- Aumentar la cobertura de pruebas.

Antes de enviar un Pull Request asegúrate de ejecutar:

```bash
python3 -m unittest discover tests
```

Todas las pruebas deben finalizar correctamente antes de enviar cambios.

---

# Documentación relacionada

- CHANGELOG.md
- LICENSE
- NOTICE

Repositorio del SDK:

https://github.com/Thrumanshow/lbh-sdk

Repositorio del protocolo:

https://github.com/Thrumanshow/Lenguaje-Binario-HormigasAIS-

Documento principal:

**LBH_SPEC_v2.0.md**

---

# Estado del proyecto

Versión actual:

**v0.3.0**

API pública validada mediante **16 pruebas automatizadas**.

---

# Roadmap

- v0.4.0 — Modularización interna
- v0.5.0 — Empaquetado oficial para Python
- v0.6.0 — SDK JavaScript
- v1.0.0 — Primera versión estable

---

# Autor

**Cristhiam Leonardo Hernández Quiñonez (CLHQ)**

Fundador de HormigasAIS

https://hormigasais.com

Nodo Maestro:

**A16 · San Miguel · El Salvador**
