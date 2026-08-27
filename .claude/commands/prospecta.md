---
description: Prospección local — encuentra negocios de una zona/sector, investiga los mejores y prepara los primeros mensajes
argument-hint: <zona> <sector> (ej. "Valencia clínicas dentales")
---

# /prospecta — Llenar el pipeline con negocio local

Prospección de $ARGUMENTS: de "no sé a quién venderle" a lista priorizada con mensajes listos.

## Proceso

1. **Busca** con `local-business-finder`: negocios de la zona/sector con sus datos (web, teléfono, reseñas). Requiere clave de gmapsscraper.io (freemium) — si no está configurada, guía el alta primero (2 min).
2. **Prioriza** (aquí está el criterio): puntúa cada negocio por señales de oportunidad — ¿web pobre o inexistente? ¿reseñas sin responder? ¿sin presencia en Maps optimizada? ¿competencia de la zona haciéndolo mejor? Un negocio con dolor visible Y capacidad de pago sube arriba.
3. **Investiga el top 5**: subagente `investigador` sobre cada uno (en paralelo). Del dossier sale el gancho específico de cada negocio.
4. **Mensajes** con `cold-email-local-business`: primer contacto personalizado por negocio — el gancho del dossier en la primera línea, oferta de valor concreta (p.ej. la /auditoria gratuita), CTA de una sola acción.
5. **Registro**: guarda la lista priorizada + dossiers + mensajes en `projects/prospeccion/<zona>-<sector>-<fecha>.md`. Los envíos y el seguimiento se llevan desde ahí (con `sales-followup` cuando toque).

## Reglas

- Calidad sobre volumen: 5 mensajes con gancho real > 50 genéricos. El operador quema su reputación local si spamea su propia ciudad.
- Cumplimiento: emails comerciales en frío en España/UE tienen límites (RGPD/LSSI) — el mensaje debe ser individual, pertinente y con identificación real. Nada de listas masivas.
