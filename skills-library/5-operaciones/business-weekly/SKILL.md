---
name: business-weekly
description: >-
  Revision operativa semanal. Analiza proyectos enviados, bloqueos, metricas clave, estado de clientes y prioridades para la siguiente semana.
  Usa cuando el usuario mencione revision semanal, weekly review, que se hizo esta semana, resumen semanal, planificar la semana, prioridades semana, o weekly.
argument-hint: "[semana opcional, ej: 2026-W12]"
---

# Revision Semanal Operativa

Ritual estructurado de cierre de semana para fundador solo o micro-equipo. Genera un informe semanal con lo enviado, lo bloqueado, metricas clave, estado de clientes y prioridades para la proxima semana.

**IDIOMA: Todo el contenido generado debe estar en espanol de Espana.**

## Cuando activar

- Viernes por la tarde o lunes a primera hora
- Cuando el usuario pida un resumen de la semana
- Cuando necesite planificar la siguiente semana
- Invocacion directa: "revision semanal", "weekly review", "que hice esta semana"

## Proceso paso a paso

### Paso 1: Cargar contexto de negocio

Lee `~/.claude/business-context.md` para conocer:
- Streams activos y sus prioridades
- Runway y situacion financiera actual
- Proyectos en curso

### Paso 2: Recopilar datos de proyectos

1. Lee `~/.claude/projects-registry.json` para obtener la lista de proyectos activos
2. Para cada proyecto registrado, lee su `.claude/backlog.md`:
   - Extrae las sesiones de trabajo de los ultimos 7 dias (busca fechas en el session log)
   - Identifica issues que cambiaron de estado (completados, en progreso, bloqueados)
   - Anota issues nuevos creados esta semana
3. Si un backlog no existe o no es accesible, anotarlo como "sin datos esta semana"

### Paso 3: Consultar Fluent Boards

1. Lee `~/.claude/fluent-boards-sync.md` para la config de API
2. Consulta el board 48 (Desarrollo Interno):
   - Tasks movidas a Done (531) en los ultimos 7 dias
   - Tasks actualmente en In Progress (530)
   - Tasks bloqueadas (534)
   - Tasks en Next (562) pendientes
3. Consulta el board 42 (Proyectos activos) para estado de clientes:
   - Tasks nuevas o urgentes esta semana
   - Tasks completadas para clientes
4. Si la API falla, usar solo los datos locales de backlog

### Paso 4: Comparar con la semana anterior

1. Lee la ultima revision semanal en `~/.claude/memory/business/weekly-reviews/`
2. Si existe, comparar:
   - Prioridades de la semana pasada vs lo que realmente se hizo
   - Bloqueos que siguen sin resolver
   - Tendencia: mas productivo, menos productivo, igual
3. Si no existe revision previa, omitir comparacion y anotar "primera revision"

### Paso 5: Generar informe

Crear archivo `~/.claude/memory/business/weekly-reviews/WEEKLY-REVIEW-{YYYY-MM-DD}.md` con esta estructura:

```markdown
# Revision Semanal — {fecha inicio} a {fecha fin}

## Que se envio esta semana

| Proyecto | Entregable | Impacto |
|----------|-----------|---------|
| ... | ... | ... |

> Resumen: X entregables en Y proyectos

## Que quedo bloqueado

| Bloqueo | Proyecto | Desde cuando | Accion necesaria |
|---------|----------|-------------|------------------|
| ... | ... | ... | ... |

> Si no hay bloqueos: "Sin bloqueos activos — buen ritmo."

## Metricas clave

- **Tasks completadas**: X (semana pasada: Y)
- **Tasks creadas**: X
- **Ratio completadas/creadas**: X (>1 = reduciendo deuda, <1 = acumulando)
- **Proyectos tocados**: X de Y activos
- **Proyectos sin actividad**: listar los que no tuvieron sesiones

## Estado de clientes

| Cliente | Estado | Notas |
|---------|--------|-------|
| ... | Verde/Amarillo/Rojo | ... |

## Prioridades proxima semana

1. **[Prioridad 1]** — Por que es urgente, que resultado se espera
2. **[Prioridad 2]** — ...
3. **[Prioridad 3]** — ...

> Maximo 3 prioridades. Si hay mas, elegir y explicar que se pospone.

## Reflexion rapida

- Lo que funciono bien esta semana:
- Lo que no funciono:
- Un cambio para la proxima semana:

## Comparacion con semana anterior

| Metrica | Semana pasada | Esta semana | Tendencia |
|---------|--------------|-------------|-----------|
| Tasks completadas | ... | ... | ... |
| Bloqueos activos | ... | ... | ... |
| Clientes atendidos | ... | ... | ... |
```

### Paso 6: Accion concreta siguiente

Despues de generar el informe, SIEMPRE proponer:

1. **Una accion inmediata** para el bloqueo mas critico (si hay alguno)
2. **La primera tarea del lunes** — concreta, con proyecto y tiempo estimado
3. Si hay prioridades en conflicto entre streams, recomendar cual atender primero segun business-context.md (runway, prioridades declaradas)

Ejemplo: "Tu primera tarea el lunes deberia ser [X] en [proyecto] porque [razon]. Tiempo estimado: 2h."

## Reglas

- No inventar datos. Si no hay informacion de un proyecto, decir "sin actividad esta semana"
- No incluir proyectos archivados o inactivos
- Priorizar siempre segun las prioridades declaradas en business-context.md
- Si el runway es critico (<3 meses), destacar que tareas generan ingresos directos
- Ser directo y conciso — esto es para el fundador, no para un comite

## Integracion

| Cuando... | Conecta con... | Para... |
|-----------|---------------|---------|
| Hay bloqueos financieros | business-cfo | Analizar impacto en cashflow |
| Cliente en rojo | business-client | Scoring detallado |
| Demasiados streams activos | business-coach | Decidir donde poner foco |
| Trimestre terminando | business-quarterly | Alimentar revision trimestral |

<!-- Source: built-in (base: alirezarezvani/claude-skills) -->
