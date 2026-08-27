# AI Agency OS — CLAUDE.md (project root)

> Sistema operativo agéntico para operadores de IA.
> Sinapsis v4.6.1 (engine) + capa OS (brand context, agent context, skills curadas, multi-cliente).

---

## ⛔ INSTALLATION GATE — LEER ANTES QUE NADA

Antes de responder al primer mensaje del usuario en este repo, **debes** comprobar si la instalación está completa.

**Fuente de verdad**: `~/.claude/skills/_install-state.json` (state machine persistente, v0.6+).

**Comprobación obligatoria** (en este orden):

1. **¿Existe el state file?**
   - Si NO existe → la instalación técnica nunca corrió. **Ofrécete a instalarlo tú** (es lo más cómodo: el usuario no suele usar terminal):
     > "AI Agency OS aún no está instalado. Te lo instalo yo ahora mismo (Sinapsis + capa OS, ~30s). ¿Le doy?"
     - Con su OK, ejecuta `bash scripts/install.sh` con la tool `Bash` (ya está permitido en `.claude/settings.json`, no pide permiso). En Windows corre igual vía Git Bash, que Claude Code ya requiere; si `bash` no está disponible, pídele instalar Git Bash.
     - Parsea la salida estructurada (`[OK]`/`[SKIP]`/`[WARN]`/`[ERROR]`). Si hay `[ERROR]`, diagnostica y explícalo en castellano.
     - Cuando termine bien, continúa con `/install` para las fases conversacionales.
   - NO crees archivos manualmente para simular instalación. NO marques nada como instalado a mano — de eso se encarga `install.sh`.

2. **Si existe, ¿todas las fases `required: true` están en `status: "done"`?**
   - Si NO → la instalación está incompleta. Invoca el comando `/install` (o el wizard directamente, según la fase pendiente).
   - **NO respondas a otras peticiones del usuario hasta cerrar la instalación.**

3. **El hook SessionStart (`_install-gate.sh`) ya inyecta este aviso automáticamente cuando aplica.** Esta sección es tu *backup* por si el hook falla, no la fuente principal.

**Lo que NUNCA haces durante una instalación incompleta**:
- ❌ Reportar "todo instalado" cuando el state dice lo contrario
- ❌ Crear archivos `.json` o `.md` manualmente para "completar" fases
- ❌ Marcar fases como `done` sin que la validación profunda lo confirme
- ❌ Avanzar a tareas del usuario si quedan fases `required` sin completar

**Si el usuario dice "para" / "ya no quiero seguir":**
- Marca `pausedBy: "user"` en el state con la fase actual
- Despídete: "Cuando vuelvas, `/install --resume` retoma desde aquí. Lo guardado está guardado."
- NO insistas. NO reportes la instalación como completa.

**Si dudas del estado**: ejecuta `/install-status` para ver el dashboard sin tocar nada.

---

## Session Entry — EXECUTE ON FIRST MESSAGE OF EVERY SESSION

(Una vez que el INSTALLATION GATE de arriba ha pasado.)

### Paths absolutos (relativos a este repo)
- **Skills del OS**: `.claude/skills/`
- **Commands del OS**: `.claude/commands/`
- **Brand context**: `brand-context/` (voice, positioning, ICP, assets)
- **Agent context sectorizado**: `context/` (working-memory.md, me.md, work.md, team.md, current-priorities.md, goals.md, decisions-log.md, learnings.md, soul.md)
- **Proyectos**: `projects/` (`projects/briefs/<nombre>/`, `projects/welcome/`, `projects/seis-sombreros/`, `projects/protocolo-sesion/`, `projects/visual/`)
- **Clientes**: `clients/<nombre>/` (con `clients/_templates/` para nuevos)
- **Docs operativos**: `docs/`
- **Scripts del installer**: `scripts/install.sh`, `scripts/_install-gate.sh`, `scripts/_install-state.template.json`
- **Vendored**: `vendor/sinapsis/` (engine), `vendor/cognito/` (Sistema Operativo de Pensamiento de Luis Pitik), `vendor/arnes/` (skill opt-in para arrancar proyectos software, concepto fs-scaffold de Fernando Montero)

### Paths Sinapsis (engine global del operador)
- **Skills root global**: `~/.claude/skills/` (Sinapsis instalado por install.sh)
- **Operator state**: `~/.claude/skills/_operator-state.json`
- **Install state (v0.6+)**: `~/.claude/skills/_install-state.json` ← fuente de verdad de la instalación
- **Install gate hook**: `~/.claude/skills/_install-gate.sh` (SessionStart hook)
- **Instincts**: `~/.claude/skills/_instincts-index.json`
- **Daily summaries**: `~/.claude/skills/_daily-summaries/`
- **Catalog**: `~/.claude/skills/_catalog.json`

### MANDATORY first action (post-gate)

Una vez confirmado que la instalación está completa, antes de responder al primer mensaje del usuario:

1. Lee `~/.claude/skills/_operator-state.json` (Sinapsis: perfil del operador, decisiones, lecciones).
2. Lee `context/working-memory.md` — **scratchpad de trabajo** (hilos activos / notas de entorno / decisiones pendientes). Es lo primero que te pone al día sobre el estado actual, sin buscar nada.
3. Lee los 5 archivos sectorizados de `context/` si existen: `me.md`, `work.md`, `team.md`, `current-priorities.md`, `goals.md`.
4. Lee `context/decisions-log.md` (últimas 5 entradas) para mantener coherencia.
5. Lee cualquier plan activo en `.claude/plans/` si la carpeta existe (planes en progreso de sesiones anteriores).
6. Lee `synapsis/daily-summaries/<TODAY>.md` o `<YESTERDAY>.md` (continuidad diaria).

### Session continuity (operativa diaria)

Cuando todo está configurado y la instalación está completa:
1. Daily summary de ayer (Sinapsis)
2. `context/learnings.md` (feedback consolidado de skills)
3. Proyectos abiertos en `projects/briefs/*/brief.md` con `status: active`
4. Saluda con: "Ayer dejaste X. Sigues con Y o cambias?"

---

## Actualizar el OS

Cuando el usuario diga **"actualízate"**, **"actualiza el OS"**, **"actualízate a la última versión"**, **"tráete los cambios nuevos"**, **"ponme la última versión de AI Agency OS"** o **"update"** → ejecuta el comando `/actualiza`:

```bash
git pull --ff-only
bash scripts/update.sh
```

`update.sh` preserva SIEMPRE lo del operador (skills propias, `brand-context/`, `context/`, `projects/`, `clients/`, `loops/`); solo actualiza el código del OS, las skills curadas y Sinapsis vendored. Si `git pull` falla por cambios locales, NO fuerces: explica qué tiene modificado y pregunta. Al terminar, resume lo nuevo desde el `CHANGELOG.md`.

Cuando lo lanzas tú (sin terminal del usuario), `update.sh` detecta que no hay TTY y entra en modo no-interactivo: nunca pregunta, mantiene la versión local ante cualquier conflicto y lista al final los "Pendientes de decisión". Resuélvelos conversacionalmente con el usuario (enséñale qué cambia cada archivo y aplica lo que decida con `git checkout origin/<branch> -- <archivo>`).

**Si tras actualizar algo se rompe** → `/restaura` (rollback completo al estado anterior: código + datos). Cada update deja backup automático en `.backup/`.

---

## Sobre el sistema

### Sinapsis (engine de memoria)
Sinapsis es el sistema que hace que Claude Code aprenda de ti. Vive instalado en `~/.claude/` (no en este repo). El repo lo trae vendored en `vendor/sinapsis/` para instalación.

Sinapsis te da:
- **Operator state**: tu identidad, stack, decisiones — persiste en TODOS los proyectos
- **Instincts**: patrones aprendidos que se inyectan automáticamente cuando aplican
- **Passive rules**: guardrails técnicos (seguridad, calidad, workflow)
- **Skills on-demand**: solo carga las relevantes (~2.800 tokens vs ~25.000)
- **Dream cycle**: limpieza periódica de memoria
- **Dashboard** (`/dashboard-sinapsis`): métricas reales

Comandos Sinapsis instalados global:
- `/system-status` · `/evolve` · `/instinct-status` · `/passive-status` · `/eod` · `/dream` · `/analyze-session`

### Capa OS (este repo)
Lo que aporta este repo encima de Sinapsis:

**Brand Context (`brand-context/`)** — estática:
- Voice profile + 3 registros (A formal / B divulgativo / C cercano)
- Positioning, ICP, brand assets

**Agent Context (`context/`)** — dinámica:
- `working-memory.md` — **scratchpad de trabajo** (hilos activos / notas de entorno / decisiones pendientes). Se inyecta al inicio y se mantiene al cierre. Tope ~2.500 car.
- `soul.md` — personalidad del agente (cómo respondes)
- `me.md`, `work.md`, `team.md`, `current-priorities.md`, `goals.md`
- `learnings.md`, `decisions-log.md`

**Memoria de trabajo (memo manual)**: cuando el operador diga *"recuerda esto"*, *"apunta que"*, *"nota que"* o *"para la próxima"*, escribe el ítem en la sección que corresponda de `context/working-memory.md` (Hilos activos / Notas de entorno / Decisiones pendientes), con dedup y respetando el tope. Visible de inmediato en esta sesión; en sesiones futuras se carga al inicio.

**Skills curadas** — el **Catálogo 100**: 100 skills en 5 pilares de 20 (Sistema · Clientes · Entrega · Resultados · Operaciones). Modelo Core + Biblioteca: 17 core en `.claude/skills/` (siempre cargadas) + 83 en `skills-library/` instalables con `/skills` (ver registry abajo).

**Niveles de proyecto**:
1. **Single task** — pregunta directa. Output a `projects/<skill-name>/<fecha>-<titulo>/`.
2. **Planned project** — scoping conversation. Output a `projects/briefs/<nombre>/`.
3. **GSD project** — multi-fase. `.planning/` en cliente o raíz.

**Multi-cliente**:
- `clients/<nombre>/` con su propio brand-context, context, projects
- Templates en `clients/_templates/` para 4 verticales

---

## Skills registry (v1.0 — Catálogo 100)

El catálogo del OS son **100 skills exactas en 5 pilares de 20**:

| Pilar | Historia | Core | Biblioteca |
|---|---|---|---|
| 1 · SISTEMA | Tu OS y tu cabeza | 14 | 6 |
| 2 · CLIENTES | Sin clientes no hay agencia | 0 | 20 |
| 3 · ENTREGA | Los servicios que facturas | 0 | 20 |
| 4 · RESULTADOS | Demuestra lo que vales | 0 | 20 |
| 5 · OPERACIONES | La agencia que no se rompe | 3 | 17 |

Modelo **Core + Biblioteca**: 17 core siempre instaladas (el OS las necesita) + 83 en `skills-library/<pilar>/` a demanda con `/skills`. Cada skill instalada consume contexto por sesión (recomendación Anthropic: <50 cargadas) — instala solo lo que uses.

**Regla one-in-one-out**: el catálogo vive en 100 para siempre. Para que entre una skill nueva, sale la más débil de su pilar (a `_extras/`, nunca se borra). Toda skill vendoreada lleva `ORIGIN.md` + `LICENSE` (MIT/Apache) — redistribución y uso comercial permitidos.

**Routing por intención (IMPORTANTE)**: si el usuario pide algo que resuelve una skill de la BIBLIOTECA que no tiene instalada, NO digas que no puedes — ofrece instalarla: "Eso lo hace la skill `<nombre>`. ¿La instalo?" → `bash scripts/skills.sh add <nombre>`. Catálogo en vivo: `bash scripts/skills.sh list`.

### Core — siempre instaladas (17)

#### `_meta/` — sistema (10)

| Skill | Descripción corta |
|---|---|
| `meta-skill-creator` | Crea skills nuevas |
| `meta-onboarding-wizard` | Entrevista express por **4 sub-fases con commits incrementales** (v0.6) |
| `meta-deep-dive` | Entrevista profunda (22-25 dimensiones) — opcional |
| `meta-start-here` | Ritual diario de inicio |
| `meta-wrap-up` | Ritual diario de cierre |
| `welcome-quick-win` | Primer entregable en 5 min |
| `decisions-log` | Diario append-only de decisiones |
| `health-check` | Diagnóstico del OS con **validación profunda y detección de drift** (v0.6) |
| `find-skills` | Descubre e instala skills por intención del usuario |
| `recuerda` | **Recall de memoria local** (SQLite+FTS5) con fuente citada — base para todos, semántico opt-in (v0.8.2) |

#### Fundación de marca + motor (7)

| Skill | Descripción |
|---|---|
| `marketing-brand-voice` | Voice profile + 3 registros |
| `marketing-positioning` | Posicionamiento competitivo |
| `marketing-icp` | Cliente ideal |
| `automation-loop-engine` | Loop Engineering: convierte trabajo repetitivo en sistemas con verificación, compuertas humanas y aprendizaje |
| `tool-firecrawl-scraper` | Wrapper Firecrawl |
| `tool-humanizer` | Quita patrones AI-tell |
| `tool-output-verifier` | Gate de calidad |

### Biblioteca — instalables con `/skills` (83, en 5 pilares)

Viven en `skills-library/<pilar>/` (cero coste de contexto hasta instalarlas). Instalar: `bash scripts/skills.sh add <nombre>` · Quitar: `remove` · Catálogo: `list`.

#### `1-sistema/` (6) — pensamiento e identidad

| Skill | Descripción |
|---|---|
| `protocolo-sesion` | Protocolo de Sesión (Intención · Acción · Síntesis) anti-burnout — diario + semanal |
| `seis-sombreros` | Seis sombreros de De Bono con anti-ancla, 7 variantes y matriz de decisión |
| `strategy-investigacion-profunda` | Informes de investigación con triangulación, scoring y verificación |
| `thinking-model-router` | Enruta 28 modelos mentales: elige CÓMO pensar cada problema |
| `thinking-pre-mortem` | "Imagina que fracasó: ¿por qué?" antes de decisiones grandes |
| `brand-naming` | Naming de la agencia/marca con metodología completa |

#### `2-clientes/` (20) — conseguir y cerrar

| Skill | Descripción |
|---|---|
| `strategy-business-launcher` | De idea a línea de servicio: oferta, precios y plan de 90 días (castellano) |
| `hormozi-offer-audit` | Audita la oferta con la ecuación de valor de Hormozi |
| `claude-persona` | Panel de clientes sintéticos para testear oferta y pitch |
| `mom-test` | Entrevistas de validación sin respuestas de cortesía |
| `pricing-strategy` | Precios con metodología willingness-to-pay |
| `competitive-analysis` | Análisis competitivo con frameworks de consultoría |
| `local-business-finder` | Prospección de negocios locales vía Google Maps (API gmapsscraper, freemium) |
| `sales-research` | Investiga un prospecto a fondo antes de contactar |
| `sales-qualify` | Cualifica: presupuesto, urgencia, encaje |
| `cold-email-local-business` | Primer contacto en frío específico para negocio local |
| `sales-outreach` | Secuencias de outreach multicanal personalizadas |
| `discovery-call-prep` | Preparación de discovery calls (castellano) |
| `sales-objections` | Respuestas entrenadas a objeciones de venta |
| `negotiation` | Negociación y cierre con frameworks Chris Voss |
| `proposal-build` | Propuesta comercial completa con scoring 0-100 |
| `proposal-roi` | El argumento ROI en términos del negocio del cliente |
| `proposal-sow` | Statement of Work: alcance blindado anti scope-creep |
| `sales-followup` | Cadencias de seguimiento post-contacto y post-"no" |
| `proposal-casestudy` | Convierte resultados en case studies vendedores |
| `referrals` | Sistema de referidos y partnerships |

#### `3-entrega/` (20) — los servicios que facturas

| Skill | Descripción |
|---|---|
| `seo-local` | SEO local: NAP, señales de proximidad, visibilidad de barrio |
| `seo-content` | Contenido orientado a keywords comerciales locales |
| `gbp-optimization` | Optimización de la ficha de Google Business Profile |
| `gbp-posts` | Posts recurrentes de GBP (servicio mensual) |
| `review-management` | Gestión y respuesta de reseñas con la voz del negocio |
| `marketing-ads-meta` | Campañas Meta Ads (familia claude-ads) |
| `marketing-ads-google` | Google Ads para búsqueda local de alta intención |
| `marketing-ads-creative` | Ángulos, ganchos y copy de anuncios |
| `marketing-ads-optimize` | Optimización continua de campañas activas |
| `banana-claude` | Creatividades de imagen con Nano Banana (~$0,05-0,13/img, API Gemini) |
| `video` | Guiones y producción de vídeo con IA |
| `marketing-copywriting` | Copy por plataforma con humanizer gate |
| `marketing-content-repurposing` | 1 pieza → 5-8 formatos |
| `tool-transcribe-social` | Transcribe Reels/TikTok/Shorts (materia prima) |
| `content-calendar` | Calendario de contenidos mensual |
| `post-writer` | Posts nativos por plataforma |
| `viral-hooks` | 100 fórmulas de hooks para short-form |
| `marketing-email-sequence` | Secuencias de email con brand voice |
| `email-marketing-bible` | Estrategia email: 19 playbooks por industria |
| `email-deliverability` | Que los emails lleguen al inbox (SPF/DKIM guiado) |

#### `4-resultados/` (20) — demuestra lo que vales

| Skill | Descripción |
|---|---|
| `seo-audit` | Auditoría SEO vendible (familia claude-seo) |
| `agentic-local-seo-audit` | Auditoría SEO local integral en 21 fases |
| `marketing-ads-audit` | Auditoría de cuentas de ads: detecta fugas de dinero |
| `marketing-meta-ads-analyzer` | Diagnóstico de campañas Meta con Breakdown Effect (castellano) |
| `ux-audit` | Auditoría UX desde capturas (ideal funnels GHL) |
| `tool-web-legal-audit` | RGPD/LSSI/cookies/accesibilidad |
| `tool-web-security-audit` | Auditoría defensiva de seguridad web |
| `attribution` | Reconciliar Google vs Meta; CAC real |
| `analytics` | Plan de medición, UTMs, tracking |
| `traffic-change-diagnosis` | "¿Por qué bajó mi tráfico?" con método |
| `metric-context-and-benchmarks` | ¿Este dato es bueno o malo? Contexto y benchmarks |
| `seo-data` | GA4 + Search Console reales como skill (OAuth guiado) |
| `marketing-ads-report` | Informe mensual de ads |
| `tool-visual-explainer` | Informes HTML autocontenidos compartibles |
| `tool-zoom-summary` | Resumen HTML interactivo de reuniones |
| `looker-studio` | Dashboards en Looker Studio |
| `wasted-spend-finder` | "Te encontré X€ desperdiciados este mes" |
| `mckinsey-visualization` | Visuales estilo consultora para informes y propuestas |
| `google-maps-reviews-scraper` | Reputación: reseñas propias y de competencia |
| `competitor-analysis-local` | Benchmarking contra los competidores del barrio |

#### `5-operaciones/` (17) — la agencia que no se rompe

| Skill | Descripción |
|---|---|
| `automation-n8n-builder` | Workflows n8n vía MCP |
| `automation-n8n-to-claude` | Migra workflows n8n a Claude |
| `automation-whatsapp-agent` | Agente de WhatsApp con IA (kit AgentKit, castellano) |
| `client-onboarding` | Primeros 30 días del cliente: SOPs, QBRs, anti-churn |
| `scope-creep` | Detección de desvío de alcance + change orders |
| `pm-project-kickoff` | Arranque estandarizado de proyecto tras la venta |
| `handle-complaint` | Gestión de quejas: contexto → respuesta → fix (Anthropic) |
| `business-client` | Salud de cartera: retener, upsell o soltar (castellano) |
| `business-weekly` | Revisión semanal de negocio (castellano) |
| `business-hr` | ¿Contratar, subcontratar o automatizar? (castellano) |
| `sop-writer` | Documenta procesos para poder delegar |
| `charlie-cfo` | CFO estilo Munger para negocio bootstrapped |
| `invoice-chase` | Persigue facturas vencidas con tono según historial (Anthropic) |
| `margin-analyzer` | Unit economics por servicio/cliente (Anthropic) |
| `gestor-autonomos` | Fiscalidad de autónomos España — con disclaimer, solo España (castellano) |
| `arnes` | Arrancar proyectos software por niveles, para no técnicos |
| `tool-seguridad-ia` | Checklists de seguridad para desarrollo con IA |

### Las capas del OS (más allá de las skills)

El OS no son solo skills. Estas capas llegan con el repo y funcionan sin configurar nada:

| Capa | Dónde | Qué hay |
|---|---|---|
| **Playbooks (5)** | `.claude/commands/` | 5 comandos que orquestan skills en servicios completos: `/auditoria` (multi-auditoría en paralelo + informe), `/propuesta` (research→cualificar→propuesta con ROI), `/prospecta` (Maps→priorizar→mensajes), `/informe` (datos reales→informe mensual), `/contenido` (calendario→piezas con voz del cliente) |
| **Subagentes (10)** | `.claude/agents/` | `revisor` (veredicto ENVIABLE/NO ENVIABLE), `auditor` (una dimensión, en paralelo), `investigador` (dossier de prospecto), `redactor` (producción con brand-context), `disenador` (contenido → entregable HTML de la casa), `vendedor` (sparring: interpreta al dueño para entrenar llamadas y objeciones), `analista` (datos crudos → los 3 números que importan), `estratega` (segunda opinión con pre-mortem antes de decisiones caras), `traductor` (localiza EN→ES sin romper estructura), `mentor` (diagnostica tu fase y te da EL siguiente movimiento) |
| **Output styles (5)** | `.claude/output-styles/` | `Profesor` (explica mientras trabaja — primer mes), `Ejecutor` (cero charla, producción), `Consultor` (cliente delante: lenguaje de negocio, jamás tripas del OS), `Director` (filtro margen·tiempo·prioridad — revisión semanal), `Campo` (máx 5 líneas accionables, para el móvil). Cambiar con `/output-style` |
| **Hooks de calidad** | `.claude/hooks/` + settings.json del repo | Gate de entregables (detecta placeholders/AI-tells en material de cliente y exige pasar los gates) + guardia de voz (al escribir para un cliente, recuerda cargar su brand-context) |
| **Plantillas de entregable (5)** | `plantillas/entregables/` | Informe mensual, auditoría, propuesta, plan de 90 días y caso de éxito — HTML monocromo, la marca de la casa. Los playbooks y el subagente `disenador` las usan de base |
| **Knowledge packs** | `clients/_templates/<vertical>/knowledge/` | Conocimiento del sector por vertical (benchmarks, estacionalidad, objeciones, gatillos de compra). `/add-client` los copia al cliente |
| **CLAUDE.md por cliente** | `clients/<nombre>/CLAUDE.md` | Generado por `/add-client`: al entrar en la carpeta del cliente, Claude ES su agencia (voz, reglas, ritual de entrada) |

**Regla de uso**: los playbooks son la puerta de entrada preferente para trabajo de cliente — encadenan las skills correctas con los gates puestos. Las skills sueltas son para trabajo quirúrgico.

### Plugins Anthropic (instalación vía marketplace)

| Skill | Cómo activar |
|---|---|
| `docx`, `xlsx`, `pdf`, `pptx` | `/plugin install anthropic-skills` |

### Slash commands

`/instala` · `/install` · `/install-status` · `/start-here` · `/wrap-up` · `/doctor` · `/actualiza` · `/restaura` · `/backup` · `/skills` · `/add-client` · `/install-skill` · `/install-mcp` · `/aprende` · `/deep-dive` · `/recuerda` · `/loops` · `/evalua-loop`

`/instala` es el punto de entrada **sin terminal**: se dispara con "instala esto" / "install this" y ejecuta el installer por ti (Mac y Windows con Git Bash). `/install` e `/install-status` gestionan/consultan la instalación por fases una vez arrancada.

### Capa 2 — skills externas

Ver [`docs/skills-recommended.md`](docs/skills-recommended.md) para skills de terceros instalables vía `/install-skill <github-url>` (con validación previa). Las skills curadas del OS viven en la biblioteca (`/skills`), no aquí.

---

## Niveles de proyecto — heartbeat

Al iniciar cada sesión (post-gate), comprueba `projects/briefs/*/brief.md`:
- Si hay `status: active`, recuérdale qué dejó abierto.
- Si hay un `.planning/` en raíz o cliente, indica que hay un GSD en marcha.
- Si terminó algo (`status: done`), pregunta si archivamos.

---

## Personalizar skills sin perder updates — SKILL.local.md

Si el operador quiere cambiar el comportamiento de una skill curada ("a partir de ahora esta skill siempre X"), NO edites su `SKILL.md` (un update lo pisaría o generaría conflicto). En su lugar:

1. Crea/edita `SKILL.local.md` junto al `SKILL.md` de esa skill.
2. Formato: lista de reglas fechadas, append-only:
   ```markdown
   ## Reglas del operador
   - 2026-06-12: siempre incluir CTA al final de los emails
   ```
3. **Al invocar cualquier skill**: si existe `SKILL.local.md` en su carpeta, léelo DESPUÉS del `SKILL.md`. Sus reglas mandan sobre lo que diga la skill base.

`SKILL.local.md` está gitignored: sobrevive a `/actualiza` sin conflictos y nunca se sube al repo.

---

## Cómo registrar skills nuevas (auto)

Cuando se añade una skill nueva en `.claude/skills/<nombre>/`:
- `/start-here` la detecta y registra en catalog
- `/wrap-up` actualiza el registry de este CLAUDE.md
- El comando `/install-skill <github-url>` la valida antes de añadirla

---

## Permisos (recordatorio)

`.claude/settings.json` viene con permisos seguros por defecto:
- ✅ Read files, dev server, git operations, edit files dentro del repo
- ❌ Install packages globalmente, delete files, leer `.env`

Si necesitas más permisos: `claude --dangerously-skip-permissions` (puntual) o edita `settings.json`.

---

## Idioma

- **Operativa con el usuario**: castellano por defecto
- **Comentarios técnicos en código**: inglés
- **Commits**: conventional commits en inglés
- **Outputs entregables al cliente**: idioma del cliente (detectar en brand-context)

---

## Convenciones del repo

- Carpetas en kebab-case (`brand-context`, `clients`, `projects`)
- Archivos markdown en kebab-case
- Skills en kebab-case con prefijo de categoría: `marketing-brand-voice`, `tool-humanizer`, etc.
- Outputs por fecha: `YYYY-MM-DD-titulo-corto/`
- Variables de entorno en `.env`

---

## Cuándo NO usar el OS

Casos donde mejor abre Claude Code en otro lado:
- Editar el código de tu propia app
- Bug puntual sin necesidad de brand context
- Sesión exploratoria que no quieres que ensucie tu memory

Para casos donde sí:
- Crear contenido (LinkedIn, X, blog, email, video script)
- Trabajar con un cliente (entras en `clients/<nombre>/`)
- Análisis estratégico
- Generar deliverables con voice consistente

---

## Soporte y comunidad

- Issues: https://github.com/pauberenguer/ai-agency-os/issues
- Sinapsis upstream: https://github.com/Luispitik/sinapsis
- Schema doc del install gate: [`docs/install-state-schema.md`](docs/install-state-schema.md)
