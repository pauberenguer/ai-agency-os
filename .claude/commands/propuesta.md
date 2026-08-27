---
description: Propuesta comercial completa para un prospecto — research + cualificación + propuesta con ROI, lista para enviar
argument-hint: <prospecto-o-negocio>
---

# /propuesta — De prospecto a propuesta enviable

Genera la propuesta comercial para $ARGUMENTS, con datos reales del negocio y argumento de ROI.

## Proceso

1. **Dossier**: lanza el subagente `investigador` sobre el prospecto. Si ya existe dossier reciente en contexto o en `projects/`, úsalo — no dupliques.
2. **Cualifica** con `sales-qualify`: si el prospecto NO cualifica (sin presupuesto, sin urgencia, mal encaje), PARA y dilo con el porqué — una propuesta a quien no va a comprar es tiempo muerto. Este comando también sirve para decidir NO enviar.
3. **Construye** con `proposal-build`: propuesta completa con scoring. Usa el dossier: dolores detectados, el gancho, el servicio del catálogo que encaja.
4. **ROI** con `proposal-roi`: traduce el precio a impacto de SU negocio ("X horas/mes ahorradas, ~Y reservas más"). Sin ROI creíble no se envía.
5. **Alcance** con `proposal-sow`: entregables, límites y qué NO incluye — el antídoto del scope creep se firma aquí, no se sufre después.
6. **Formato**: monta el documento final sobre `plantillas/entregables/propuesta.html`. Una página de lectura, no un tocho.
7. **Gate**: subagente `revisor`. Si el veredicto es NO ENVIABLE, arregla y repite.

## Reglas

- Precios: si el operador no ha definido pricing, ofrece correr `pricing-strategy` antes — nunca inventes tarifas.
- La propuesta cita SIEMPRE algo específico del negocio del prospecto (del dossier). Propuesta genérica = propuesta ignorada.
