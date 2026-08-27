# Origen de esta skill

Esta skill viene del repositorio externo:

- **Repositorio**: [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads)
- **Skill original**: `skills/ads-creative/`
- **Autor**: Daniel Agrici
- **Licencia**: MIT (ver `LICENSE` en esta carpeta)
- **Fecha de vendoreo**: 2026-08-27

## Cambios respecto al original

- Renombrada `ads-creative` → `marketing-ads-creative` (convención AI Agency OS)
- Resto del contenido idéntico (en inglés, como el original)

## Nota

El upstream tiene 33 skills para 12 plataformas de ads. Aquí vendoreamos las 6
relevantes para el programa (audit, meta, google, creative, report, optimize).
Si necesitas otra plataforma (TikTok, LinkedIn, YouTube...), vendorea igual.

## Cómo se actualiza

1. Clonar el repo origen y hacer diff con la versión vendoreada.
2. Si los cambios son relevantes, actualizar SKILL.md conservando el rename del `name:`.
