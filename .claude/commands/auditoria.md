---
description: Auditoría completa de un negocio local (SEO + UX + legal + seguridad + ads) con informe unificado — la puerta de entrada comercial
argument-hint: <web-o-negocio> [cliente]
---

# /auditoria — La puerta de entrada comercial

Auditoría multi-dimensión de $ARGUMENTS con informe final vendible. Es EL entregable con el que un operador abre puertas: se regala o se cobra, y de él salen los primeros retainers.

## Proceso

1. **Alcance** (30 seg): confirma la web/negocio y qué dimensiones aplican. Por defecto: SEO local + UX + legal. Añade seguridad si la web tiene formularios/pagos, y ads solo si hay acceso a cuentas.
2. **Instala lo que falte**: comprueba con `bash scripts/skills.sh list` que las skills necesarias están instaladas (`seo-audit` o `agentic-local-seo-audit`, `ux-audit`, `tool-web-legal-audit`, `tool-web-security-audit`, `marketing-ads-audit`). Ofrece instalar las que falten.
3. **Lanza los auditores EN PARALELO**: un subagente `auditor` por dimensión, cada uno con su encargo claro. No las hagas en serie — el paralelo es el 80% del valor de este comando.
4. **Fusiona**: consolida los hallazgos en un único documento — nota global, top 5 críticos entre TODAS las dimensiones (priorizados por impacto en el negocio, no por dimensión), quick wins, y plan de 30 días.
5. **Informe**: genera el HTML final con `tool-visual-explainer` usando la plantilla `plantillas/entregables/auditoria.html` como base visual. Lenguaje de dueño de negocio.
6. **Gate**: pásalo por el subagente `revisor` antes de darlo por terminado. Si hay cliente ($2), guárdalo en `clients/$2/entregables/`.

## Reglas

- Solo webs propias o con autorización del dueño (la parte de seguridad lo exige — está en su skill).
- Cero hallazgos inventados: lo no verificable se marca como tal.
- El informe termina SIEMPRE con siguiente paso comercial claro (la llamada, la propuesta).
