---
name: business-client
description: >-
  Scoring de salud de clientes activos en 5 dimensiones. Identifica riesgos de churn, oportunidades de upsell y clientes que soltar.
  Usa cuando el usuario mencione clientes, client health, scoring clientes, churn, upsell, cartera de clientes, estado clientes, o client review.
argument-hint: "[nombre de cliente opcional para analisis individual]"
---

# Scoring de Salud de Clientes

Sistema de evaluacion de la cartera de clientes para fundador solo o micro-agencia. Puntua cada cliente activo en 5 dimensiones, identifica semaforos, y recomienda acciones concretas: retener, hacer upsell, o soltar.

**IDIOMA: Todo el contenido generado debe estar en espanol de Espana.**

## Cuando activar

- Revision mensual o trimestral de la cartera
- Cuando un cliente empieza a dar problemas (impagos, scope creep, comunicacion rota)
- Antes de decidir si aceptar mas trabajo de un cliente existente
- Cuando hay que decidir a quien priorizar con recursos limitados
- Invocacion directa: "scoring clientes", "client health", "estado de clientes"

## Las 5 dimensiones (1-5 puntos cada una)

### 1. Fiabilidad de ingresos

Mide: paga a tiempo, volumen consistente de trabajo, previsibilidad.

| Puntos | Criterio |
|--------|----------|
| 5 | Paga siempre a tiempo, trabajo recurrente estable, contrato claro |
| 4 | Paga a tiempo, trabajo frecuente pero sin contrato fijo |
| 3 | Paga con retrasos leves (<15 dias), trabajo esporadico |
| 2 | Retrasos frecuentes (>15 dias), trabajo impredecible |
| 1 | Impagos, hay que perseguir facturas, trabajo puntual y mal pagado |

### 2. Calidad de comunicacion

Mide: responde a tiempo, briefings claros, feedback constructivo, respeta tu tiempo.

| Puntos | Criterio |
|--------|----------|
| 5 | Responde en <24h, briefings escritos y claros, feedback especifico |
| 4 | Responde en <48h, briefings razonables, feedback util |
| 3 | Responde en <1 semana, briefings ambiguos, feedback vago |
| 2 | Tarda >1 semana, sin briefings, feedback contradictorio |
| 1 | Desaparece semanas, no da briefings, cambia de opinion constantemente |

### 3. Disciplina de scope

Mide: respeta los limites del proyecto o hay scope creep constante.

| Puntos | Criterio |
|--------|----------|
| 5 | Nunca pide trabajo fuera de scope, entiende que lo extra se presupuesta aparte |
| 4 | Pide extras ocasionalmente, acepta presupuesto adicional sin problema |
| 3 | Scope creep frecuente pero lo acepta cuando se senala |
| 2 | Scope creep constante, se resiste a pagar extras |
| 1 | Espera trabajo ilimitado por un precio fijo, discute cada factura |

### 4. Potencial de crecimiento

Mide: posibilidad de upsell, referidos, relacion a largo plazo, valor estrategico.

| Puntos | Criterio |
|--------|----------|
| 5 | Multiples proyectos posibles, da referidos activamente, relacion estrategica |
| 4 | Hay oportunidades claras de upsell, potencial de referidos |
| 3 | Un proyecto mas posible, sin referidos pero buena relacion |
| 2 | Poco recorrido, relacion transaccional |
| 1 | Sin futuro, proyecto puntual, no refiere ni referira |

### 5. Balance de energia

Mide: trabajar con este cliente te da energia o te la quita.

| Puntos | Criterio |
|--------|----------|
| 5 | Disfruto el trabajo, proyectos interesantes, relacion positiva |
| 4 | Trabajo agradable, sin estres significativo |
| 3 | Neutral — ni positivo ni negativo |
| 2 | Genera estres, trabajo tedioso o conflictos frecuentes |
| 1 | Dreading — cada email suyo genera ansiedad, trabajo toxico |

## Proceso paso a paso

### Paso 1: Cargar contexto

1. Lee `~/.claude/business-context.md` — streams, clientes mencionados, prioridades
2. Lee `~/.claude/projects-registry.json` — proyectos activos por cliente

### Paso 2: Consultar Fluent Boards

1. Lee `~/.claude/fluent-boards-sync.md` para la config de API
2. Consulta board 42 (Proyectos activos):
   - Lista todas las tasks agrupadas por cliente (usa labels)
   - Cuenta tasks abiertas vs completadas por cliente
   - Identifica tasks urgentes o con mucho tiempo abiertas
   - Identifica labels: Soporte, Proyecto, Mantenimiento, Urgente, Recurrente
3. Si la API falla, pedir al usuario que enumere sus clientes activos

### Paso 3: Pedir datos al usuario

Para cada cliente activo, si no hay datos suficientes en el board, preguntar:

- "Con {cliente}: paga a tiempo? volumen de trabajo? hay scope creep?"
- No hacer un interrogatorio — agrupar preguntas por cliente, maximo 3 preguntas por cliente
- Si el usuario pide analisis de un solo cliente, profundizar solo en ese

### Paso 4: Scoring y semaforo

Calcular puntuacion total por cliente (suma de las 5 dimensiones):

| Rango | Semaforo | Significado |
|-------|----------|-------------|
| 20-25 | Verde | Cliente estrella. Cuidar y hacer crecer |
| 13-19 | Amarillo | Cliente aceptable. Vigilar las dimensiones bajas |
| 5-12 | Rojo | Cliente problematico. Evaluar si merece seguir |

### Paso 5: Generar informe

Crear/actualizar `~/.claude/memory/business/CLIENT-HEALTH.md`:

```markdown
# Scoring de Salud de Clientes

> Ultima actualizacion: {fecha}
> Clientes evaluados: {numero}

## Resumen rapido

| Cliente | Ingresos | Comunic. | Scope | Potencial | Energia | TOTAL | Estado |
|---------|----------|----------|-------|-----------|---------|-------|--------|
| ... | X/5 | X/5 | X/5 | X/5 | X/5 | XX/25 | Verde/Amarillo/Rojo |

## Detalle por cliente

### {Nombre del cliente} — {Semaforo} ({puntuacion}/25)

| Dimension | Puntuacion | Notas |
|-----------|-----------|-------|
| Fiabilidad de ingresos | X/5 | ... |
| Calidad de comunicacion | X/5 | ... |
| Disciplina de scope | X/5 | ... |
| Potencial de crecimiento | X/5 | ... |
| Balance de energia | X/5 | ... |

**Tasks abiertas**: X (Y urgentes)
**Ultimo trabajo completado**: {fecha}
**Ingresos estimados ultimos 3 meses**: {cantidad}

**Recomendacion**: {Retener / Hacer upsell / Renegociar condiciones / Soltar}
**Accion concreta**: {que hacer esta semana con este cliente}

{repetir para cada cliente}

## Alertas

### Riesgos de churn (clientes que podriamos perder)
- ...

### Oportunidades de upsell
- ...

### Clientes a soltar
- ...

## Salud general de la cartera

- **Concentracion**: {X}% de ingresos viene de un solo cliente (>40% = riesgo)
- **Distribucion de semaforos**: X verdes, Y amarillos, Z rojos
- **Nota media de la cartera**: {promedio}/25
```

### Paso 6: Accion concreta siguiente

Despues de generar el informe, SIEMPRE proponer:

1. **Para clientes rojos**: accion inmediata — renegociar, poner limites, o preparar salida
2. **Para el mejor cliente verde**: una propuesta de upsell concreta esta semana
3. **Si hay concentracion >40%**: plan para diversificar (prospeccion, producto, etc.)

Ejemplo: "Esta semana, envia un email a {cliente rojo} poniendo limites claros sobre el scope. Y propone a {cliente verde} el servicio de mantenimiento que aun no tiene."

## Reglas

- No puntuar sin datos. Si no hay informacion, marcar como "sin datos — pedir al usuario"
- La dimension "energia" es subjetiva y solo el fundador puede puntuarla — preguntar siempre
- No recomendar soltar un cliente sin considerar el impacto en el cashflow (conectar con business-cfo)
- Ser directo: si un cliente es toxico, decirlo claramente
- Actualizar CLIENT-HEALTH.md en cada ejecucion, no crear archivos nuevos

## Integracion

| Cuando... | Conecta con... | Para... |
|-----------|---------------|---------|
| Soltar un cliente afecta al cashflow | business-cfo | Simular impacto financiero |
| Hay que buscar nuevos clientes | market-proposal | Generar propuestas |
| La cartera esta desequilibrada | business-quarterly | Ajustar OKRs del trimestre |
| Cliente verde con potencial | market-emails | Secuencia de upsell |
| Fundador quemado con un cliente | business-coach | Gestion de energia y limites |

<!-- Source: built-in (base: alirezarezvani/claude-skills) -->
