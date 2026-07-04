# Guía de Contribución

¡Gracias por tu interés en LBH SDK! La interoperabilidad del protocolo depende de la colaboración abierta.

## Cómo colaborar
1. **Reportar Issues:** Si encuentras un error, abre un Issue detallando los pasos para reproducirlo.
2. **Pull Requests:** 
   - Haz un fork del repositorio.
   - Crea una rama para tu funcionalidad (`git checkout -b feature/nombre`).
   - Implementa los cambios asegurando que las pruebas pasen (`python3 -m unittest discover tests`).
   - Envía tu PR a la rama `main`.
3. **Documentación:** Toda nueva funcionalidad debe actualizar el `README.md` y el `CHANGELOG.md`.

## Estándares de Código
- Mantén la simplicidad: el LBH SDK debe seguir siendo libre de dependencias externas.
- Todo código nuevo debe incluir cobertura de pruebas en `tests/`.

---
*Autor: Cristhiam Leonardo Hernández Quiñonez (CLHQ)*
