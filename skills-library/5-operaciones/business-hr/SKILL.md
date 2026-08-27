---
name: business-hr
description: >-
  Decision de personas para micro-negocio: contratar vs externalizar vs automatizar. Evaluacion de freelancers, cuando hacer la primera contratacion, gestion de colaboradores, onboarding.
  Usa cuando el usuario mencione contratar, freelancer, VA, asistente virtual, delegar, primera contratacion, equipo, colaboradores, outsource, automatizar tareas, o hr.
argument-hint: "[rol o tarea a evaluar, ej: 'soporte tecnico' o 'primera contratacion']"
---

# Analisis de Personas — Micro-equipo

Framework de decisiones sobre personas para fundador solo o negocio de 1-3 personas. No es un departamento de RRHH — es un sistema para decidir cuando y como dejar de hacerlo todo tu solo.

**IDIOMA: Todo el contenido generado debe estar en espanol de Espana.**

## Cuando activar

- Cuando el fundador no da abasto y piensa en contratar o delegar
- Antes de publicar una oferta o buscar freelancer
- Cuando hay que evaluar si un colaborador actual funciona
- Para decidir entre automatizar, externalizar o contratar
- Invocacion directa: "necesito ayuda", "deberia contratar", "buscar freelancer", "delegar"

## Proceso paso a paso

### Paso 1: Cargar contexto

1. Lee `~/.claude/business-context.md` — runway, ingresos, streams activos
2. Lee `~/.claude/memory/business/CLIENT-HEALTH.md` si existe — carga de trabajo por cliente
3. Lee las ultimas revisiones semanales para entender la carga actual

### Paso 2: Diagnosticar la necesidad

Antes de hablar de personas, entender QUE hay que resolver. Preguntar al usuario:

**Pregunta clave**: "Que tarea o tareas te estan quitando mas tiempo y NO generan valor directo?"

Clasificar cada tarea mencionada en una de estas categorias:

| Categoria | Descripcion | Ejemplo |
|-----------|-------------|---------|
| **Core** | Solo tu puedes hacerlo, es tu ventaja competitiva | Diseno de arquitectura, relacion con clientes clave, estrategia |
| **Delegable** | Alguien con instrucciones claras podria hacerlo | Soporte nivel 1, actualizaciones WP, publicacion de contenido |
| **Automatizable** | Un script, workflow o IA podria hacerlo | Backups, facturacion recurrente, emails de seguimiento, reportes |
| **Eliminable** | No deberia hacerse en absoluto | Reuniones sin agenda, features que nadie pidio, perfeccionismo |

**Regla**: Antes de contratar a nadie, agotar automatizar y eliminar. Son gratis.

### Paso 3: El arbol de decision

```
Tarea que te quita tiempo
    |
    ├── Se puede eliminar? → Eliminarla. Fin.
    |
    ├── Se puede automatizar? (script, IA, workflow)
    |   └── Si → Automatizar. Coste unico, retorno infinito.
    |
    ├── Se puede externalizar? (freelancer puntual)
    |   └── Si → Freelancer por proyecto. Sin compromiso fijo.
    |
    ├── Es recurrente y necesita contexto continuo?
    |   └── Si → Colaborador estable (VA, freelancer a retainer)
    |
    └── Requiere dedicacion completa y genera >3x su coste en valor?
        └── Si → Primera contratacion. Leer seccion especifica.
```

### Paso 4: Analisis segun tipo de solucion

#### A) Automatizar

Para cada tarea automatizable, producir:

```markdown
### Tarea: {nombre}
- **Tiempo actual**: X horas/semana
- **Herramienta propuesta**: {nombre} o script custom
- **Coste de implementacion**: X horas una vez
- **Ahorro semanal**: X horas
- **ROI**: se amortiza en {X semanas}
- **Complejidad**: Baja (1-2h) / Media (4-8h) / Alta (>8h)
```

Priorizar automatizaciones con ROI < 4 semanas.

#### B) Externalizar (freelancer por proyecto)

Para cada tarea externalizable:

```markdown
### Tarea: {nombre}
- **Tipo de perfil**: {disenador, dev, copywriter, VA, etc.}
- **Donde buscar**: {plataformas concretas relevantes al mercado espanol}
- **Presupuesto estimado**: {rango}
- **Briefing minimo**: {que necesita saber para empezar}
- **Criterio de evaluacion**: {como saber si el resultado es bueno}
- **Riesgo principal**: {que puede salir mal}
```

#### C) Colaborador estable (VA o freelancer a retainer)

Analisis mas profundo:

```markdown
### Rol: {nombre del rol}
- **Tareas incluidas**: lista concreta
- **Horas/semana**: X
- **Coste mensual estimado**: {rango}
- **Ingresos que libera o genera**: {estimacion}
- **ROI mensual**: positivo si libera >X horas de trabajo facturable
- **Perfil ideal**: {habilidades, idioma, zona horaria, herramientas}
- **Periodo de prueba**: 2-4 semanas con tareas definidas
- **Sistema de feedback**: {como y cuando evaluar}
```

#### D) Primera contratacion

**Solo recomendar si se cumplen TODAS estas condiciones**:

1. **Ingresos estables** > 3x el coste total del empleado (salario + SS + herramientas)
2. **Carga recurrente** de >20h/semana de tareas delegables identificadas
3. **Runway** > 6 meses con el nuevo coste incluido
4. **El fundador** esta rechazando trabajo por falta de capacidad (ingresos perdidos)

Si no se cumplen todas, recomendar freelancer o VA primero.

```markdown
### Analisis de primera contratacion

**Test de viabilidad**:
- [ ] Ingresos mensuales estables: {cantidad} (necesario: >{3x coste})
- [ ] Horas delegables identificadas: {X}h/semana (necesario: >20h)
- [ ] Runway con nuevo coste: {X} meses (necesario: >6)
- [ ] Ingresos rechazados ultimo mes: {cantidad} (necesario: >0)

**Resultado**: {Viable / Prematuro / Critico (necesitas ayuda pero no puedes pagarla)}

Si es "Prematuro": empezar con freelancer a retainer 10h/semana como paso intermedio.
Si es "Critico": primero resolver el problema de ingresos (business-cfo + business-quarterly).
```

### Paso 5: Herramientas de gestion de colaboradores

Si el usuario ya tiene colaboradores o va a incorporar uno:

#### Briefing template

```markdown
## Briefing — {nombre del proyecto/tarea}

**Contexto**: {por que existe esta tarea, que problema resuelve}
**Objetivo**: {resultado esperado, concreto y medible}
**Entregable**: {que archivo/resultado se espera}
**Fecha limite**: {cuando}
**Referencia**: {ejemplos de lo que se busca, links}
**No hacer**: {errores comunes o cosas que evitar}
**Dudas**: {contactar por email/Slack, respuesta en <24h}
```

#### Checklist de onboarding para colaborador nuevo

```markdown
## Onboarding — {nombre del colaborador}

### Dia 1
- [ ] Compartir accesos necesarios (solo los minimos)
- [ ] Enviar documento de contexto del negocio (version simplificada)
- [ ] Primera tarea pequena para validar comprension
- [ ] Definir canal de comunicacion y horario de disponibilidad

### Semana 1
- [ ] 2-3 tareas reales con feedback detallado
- [ ] Reunion de 15min para resolver dudas
- [ ] Evaluar: entiende las instrucciones? cumple plazos? calidad aceptable?

### Semana 2-4
- [ ] Tareas con menos supervision
- [ ] Feedback semanal (5 min por escrito o llamada corta)
- [ ] Decision: continuar / ajustar / no continuar

### Evaluacion final (semana 4)
- [ ] Calidad del trabajo: {1-5}
- [ ] Autonomia: {1-5}
- [ ] Comunicacion: {1-5}
- [ ] Cumplimiento de plazos: {1-5}
- [ ] Decision: {seguir / renegociar / terminar}
```

#### Loop de feedback para colaboradores activos

Frecuencia: cada 2 semanas (maximo). Formato:

1. **Que esta funcionando bien** (1-2 puntos)
2. **Que mejorar** (1 punto concreto, con ejemplo)
3. **Proximas prioridades** (2-3 tareas)

No hacer revisiones formales ni frameworks corporativos. Feedback directo, frecuente y breve.

### Paso 6: Generar documento

Crear/actualizar `~/.claude/memory/business/HR-ANALYSIS.md`:

```markdown
# Analisis de Personas

> Ultima actualizacion: {fecha}
> Tareas analizadas: {numero}

## Mapa de tareas del fundador

| Tarea | Horas/semana | Categoria | Accion recomendada |
|-------|-------------|-----------|-------------------|
| ... | ... | Core/Delegable/Automatizable/Eliminable | ... |

## Total de horas por categoria

- Core (no delegable): Xh/semana
- Delegable: Xh/semana
- Automatizable: Xh/semana
- Eliminable: Xh/semana
- **Capacidad libre si se actua**: Xh/semana

## Recomendaciones

### Automatizaciones prioritarias (hacer ya)
{lista con ROI}

### Externalizaciones recomendadas
{perfiles de freelancer con coste}

### Colaborador estable (si aplica)
{analisis de VA/retainer}

### Primera contratacion (si aplica)
{analisis de viabilidad}

## Colaboradores actuales (si hay)

| Nombre | Rol | Horas/semana | Evaluacion | Estado |
|--------|-----|-------------|-----------|--------|
| ... | ... | ... | X/20 | Continuar/Ajustar/Terminar |
```

### Paso 7: Accion concreta siguiente

Despues de generar el analisis, SIEMPRE proponer:

1. **La automatizacion mas rapida** — la tarea con mayor ahorro y menor esfuerzo de implementacion
2. **Si hay tareas delegables**: redactar el briefing de la primera tarea a externalizar
3. **Si hay colaboradores existentes**: el proximo feedback a dar (con puntos concretos)

Ejemplo: "Lo primero que haria esta semana es automatizar {tarea X} con {herramienta} — te ahorra 3h/semana y se monta en 2h. Despues, publica una oferta en {plataforma} buscando {perfil} para {tarea Y}."

## Reglas

- No recomendar contratar si el runway no lo soporta. Ser brutalmente honesto
- No usar jerga de RRHH corporativo: no hay "talent acquisition", hay "encontrar a alguien bueno"
- Siempre considerar "automatizar" antes de "contratar" — una IA o un script no pide vacaciones
- El balance energia del fundador importa: si una tarea le quema, eso tiene valor economico real
- Para un negocio de 1-3 personas, la cultura es la relacion directa. No hace falta framework de cultura

## Integracion

| Cuando... | Conecta con... | Para... |
|-----------|---------------|---------|
| El coste no encaja | business-cfo | Simular impacto en cashflow |
| Hay que automatizar | business-ops | Disenar el workflow automatizado |
| No hay capacidad y hay runway | business-quarterly | Incluir contratacion en los OKRs |
| Fundador quemado | business-coach | Priorizar delegacion por energia |
| Necesita freelancers creativos | market | Buscar perfiles de marketing/diseno |

<!-- Source: built-in (base: alirezarezvani/claude-skills) -->
