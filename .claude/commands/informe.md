---
description: Informe mensual de cliente — datos reales + hallazgos + "dinero encontrado", en la plantilla de la casa
argument-hint: <cliente> [mes]
---

# /informe — El ritual que renueva contratos

Informe mensual de $ARGUMENTS. Es el momento donde el cliente decide si sigues otro mes: se escribe para demostrar valor, no para listar tareas.

## Proceso

1. **Contexto**: lee `clients/$1/` (qué servicios tiene contratados, informes anteriores en `entregables/`, decisiones del log). El informe continúa una historia, no empieza de cero.
2. **Datos reales**: tira de los MCPs conectados (GA4/GSC/Meta — ver `docs/mcps-curated.md`) o pide los exports al operador. Sin datos no hay informe: si no hay nada conectado, ofrece configurarlo primero.
3. **Interpreta con criterio**: usa `metric-context-and-benchmarks` (¿esto es bueno o malo?) y, si algo cayó, `traffic-change-diagnosis` (el porqué con método, no excusas).
4. **Busca el titular**: corre `wasted-spend-finder` si hay ads — "hemos encontrado y cortado X€ de gasto desperdiciado" es la frase que renueva contratos. Si no hay ads, el titular es el avance más tangible del mes en lenguaje de negocio.
5. **Monta** sobre `plantillas/entregables/informe-mensual.html`: titular del mes → 3 números que importan (con comparativa) → qué hicimos → qué haremos → recomendación. UNA página de lectura.
6. **Gate**: subagente `revisor`. Guarda en `clients/$1/entregables/YYYY-MM-informe.html`.

## Reglas

- Números SIEMPRE con contexto ("+18% visitas desde Maps vs julio") y en impacto ("≈ 30 llamadas más").
- Mes malo: se cuenta de frente, con diagnóstico y plan. Un cliente perdona un mes malo; no perdona enterarse tarde.
- Cero relleno de actividad ("publicamos 12 posts") sin su resultado al lado.
