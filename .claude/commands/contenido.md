---
description: El mes de contenido de un cliente — calendario + piezas escritas con su voz + ganchos, listo para programar en GHL
argument-hint: <cliente> [mes]
---

# /contenido — El retainer de redes, ejecutado

Produce el mes de contenido de $ARGUMENTS: calendario aprobado primero, piezas después.

## Proceso

1. **Brand-context primero**: lee `clients/$1/brand-context/` (voz, ICP, posicionamiento). Si no existe, PARA y ofrécele generarlo (`marketing-brand-voice` + `marketing-icp`) — contenido sin voz definida es contenido genérico que el cliente rechazará.
2. **Calendario** con `content-calendar`: propón el mes (temas, formatos, frecuencia por canal) apoyado en `content-strategy` si es el primer mes. **Espera el OK del operador antes de producir** — corregir un calendario cuesta 5 min; corregir 20 piezas, una tarde.
3. **Producción**: lanza el subagente `redactor` con el calendario aprobado. Posts con `post-writer`, ganchos de short-form con `viral-hooks`, y si hay pieza larga del cliente (vídeo, entrevista), `marketing-content-repurposing` la multiplica en derivadas.
4. **Gates**: cada pieza pasa `tool-humanizer` (que no huela a IA) y el lote completo pasa el subagente `revisor`.
5. **Entrega**: guarda en `clients/$1/entregables/YYYY-MM-contenido/` organizado por canal y fecha, listo para programar en el Social Planner de GHL (la publicación vive ahí, no aquí).

## Reglas

- La voz del cliente manda. En la duda entre "queda mejor" y "suena a él": suena a él.
- Cada pieza con su CTA concreta. Métrica de vanidad no paga el retainer.
- Reaprovecha: 1 idea fuerte → post + carrusel + gancho de reel. El calendario se diseña así desde el principio.
