# MCPs curados para AI Agency OS

> Lista validada de Model Context Protocol servers útiles para operadores IA.
> Cada entrada incluye: para qué sirve, cuándo usarlo, instalación, riesgo de tokens, alternativas.
>
> Última revisión: 2026-06-03

## Cómo usar

```
/install-mcp <name>
```

O manualmente: copia la config a `.mcp.json` y rellena variables de entorno en `.env`.

---

## ⭐ Top 5 recomendados (instalar siempre)

### 1. context7 · Docs vivos para LLMs

**Para qué**: cuando construyes con un framework/lib (Next.js, Supabase, Tailwind, etc.), Context7 inyecta la documentación oficial actualizada en el contexto. Evita que Claude alucine APIs obsoletas.

**Cuándo activarlo**: en cualquier sesión donde escribas código con frameworks.

**Riesgo de tokens**: medio-alto si lo usas en CADA prompt. Mejor: invocarlo explícitamente con "use context7 para [tema]".

**Plan**: gratis, no requiere API key.

**Config**:
```json
"context7": {
  "command": "npx",
  "args": ["-y", "@upstash/context7-mcp"],
  "env": {}
}
```

**Variables**: ninguna.

---

### 2. github · Operaciones git y repos

**Para qué**: leer issues, PRs, archivos de cualquier repo público o tuyo. Crear/comentar issues, mergear PRs.

**Cuándo activarlo**: si trabajas con varios repos y quieres que Claude pueda actuar sobre ellos sin `gh` CLI.

**Riesgo de tokens**: bajo. Solo invoca tools cuando lo pides.

**Plan**: gratis (Personal Access Token).

**Config**:
```json
"github": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-github"],
  "env": {
    "GITHUB_PERSONAL_ACCESS_TOKEN": "$GITHUB_TOKEN"
  }
}
```

**Variables**: `GITHUB_TOKEN` (PAT con scopes: repo, read:user).

**Alternativa**: usar `gh` CLI desde Bash directamente. Más simple si solo necesitas comandos puntuales.

---

### 3. supabase · Tu base de datos

**Para qué**: queries SQL, gestión de tablas, RLS, edge functions, storage. Operador del Supabase project desde Claude.

**Cuándo activarlo**: si tienes apps en Supabase (self-hosted o cloud) y construyes con Claude Code.

**Riesgo de tokens**: bajo si configuras RLS correctamente.

**Plan**: gratis (OSS) + plan Supabase de tu proyecto.

**Config**:
```json
"supabase": {
  "command": "npx",
  "args": ["-y", "@supabase/mcp-server-supabase@latest", "--project-ref=$SUPABASE_PROJECT_REF"],
  "env": {
    "SUPABASE_ACCESS_TOKEN": "$SUPABASE_ACCESS_TOKEN"
  }
}
```

**Variables**:
- `SUPABASE_PROJECT_REF` — el ref del proyecto (en URL del dashboard)
- `SUPABASE_ACCESS_TOKEN` — token de acceso desde Account → Access Tokens

**⚠️ Importante**: usa READ-ONLY token para empezar. Solo eleva permisos cuando confíes en el flujo.

---

### 4. notion · Si trabajas en Notion

**Para qué**: leer páginas, crear bases de datos, mover páginas, crear comentarios. Si tu wiki/CRM/sistema de tareas está en Notion.

**Cuándo activarlo**: si usas Notion como home-base operativo.

**Riesgo de tokens**: medio (Notion devuelve estructuras grandes).

**Plan**: gratis hasta cierto uso (Notion Connect API).

**Config**:
```json
"notion": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-notion"],
  "env": {
    "NOTION_API_KEY": "$NOTION_API_KEY"
  }
}
```

**Variables**: `NOTION_API_KEY` (Internal Integration Token desde notion.so/my-integrations).

**⚠️ Importante**: solo da acceso a las páginas que comparta el integration. No da acceso a todo el workspace por defecto.

---

### 5. firecrawl · Scraping de webs

**Para qué**: scrapear webs con bot blockers (mejor que WebFetch nativo). Usado por `tool-firecrawl-scraper` y otras skills.

**Cuándo activarlo**: si haces investigación competitiva, brand-voice extraction, o cualquier scraping.

**Riesgo de tokens**: bajo (devuelve solo contenido principal).

**Plan**: 500 créditos free one-time. Hobby $16/mo, 3000 créditos.

**Config**: este MCP NO se invoca como MCP server de Claude Code, sino como API directa desde skills. No va en `.mcp.json`. Configuración solo en `.env`:

```bash
FIRECRAWL_API_KEY=fc-xxxxx
```

---

## 🔧 Útiles para casos específicos

### codegraph · Grafo de código local (ideal si programas)

**Para qué**: da al agente un **grafo del código** de tu proyecto (símbolos, llamadas, imports) en una SQLite local. El agente responde "¿cómo funciona X?", "¿quién llama a Y?", "¿qué rompo si cambio Z?" sin grep ni lectura masiva → menos tokens y menos tool calls.

**Cuándo activarlo**: si construyes apps o webs (Next.js, scripts…) y quieres que Claude navegue tu código de forma eficiente. Pensado para vibe-coders.

**Riesgo de tokens**: bajo — de hecho los **reduce** (benchmarks del autor: ~16% más barato, ~58% menos tool calls).

**Plan**: gratis, MIT, **100% local, sin API keys, sin servicios externos** (solo un `.db` SQLite).

**Instalación** (un comando, self-contained, cross-OS):
```bash
npm i -g @colbymchenry/codegraph    # o: curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh
codegraph install                   # auto-configura Claude Code / Cursor / Codex…
cd tu-proyecto && codegraph init -i # indexa ese proyecto
```

**Config MCP manual** (alternativa, en `.mcp.json`):
```json
"codegraph": { "type": "stdio", "command": "codegraph", "args": ["serve", "--mcp"] }
```

**Variables**: ninguna.

**✅ Validado** (2026-06-03, repo `recursos-platform`): instalación 4 s · indexado de 72 archivos en 281 ms · búsqueda + `callers` + `impact` precisos · SQLite local 1,2 MB.

**⚠️ Notas**:
- Es para **código** (TS/JS/Python/Go/Rust/Swift…), NO para memoria narrativa de negocio.
- Auto-sync con file watcher (se mantiene fresco solo). El índice `.codegraph/` va **gitignored**.

---

### composio · Cientos de integraciones en un MCP

**Para qué**: conectar Claude a herramientas SaaS (Gmail, Slack, HubSpot, Sheets,
Calendly, cientos más) sin montar un MCP por herramienta. Gestiona la
autenticación OAuth por ti.

**Cuándo activarlo**: cuando un cliente usa una herramienta para la que no hay
MCP oficial curado, o necesitas varias integraciones a la vez en un flujo.

**Riesgo de tokens**: medio — expone muchas tools; limita las apps activas a
las del caso de uso.

**Plan**: freemium, requiere cuenta en [composio.dev](https://composio.dev).

**Cuidado**: es un intermediario con acceso a tus cuentas conectadas — para
datos sensibles de cliente, valora antes un MCP oficial de la herramienta.

### linear · Gestión de proyectos

**Para qué**: si usas Linear para issue tracking en lugar de GitHub Issues.
**Plan**: gratis hasta cierto uso.
**Config**: `@modelcontextprotocol/server-linear`

### gmail · Lectura de emails

**Para qué**: leer/buscar emails, crear drafts. NO enviar (eso requiere user explicit ok).
**Plan**: gratis con Google Workspace.
**Config**: requiere OAuth setup más complejo.
**Riesgo**: alto si das write permissions. Mantén READ-ONLY hasta confiar.

### slack · Mensajería interna

**Para qué**: leer canales, crear posts, threads. Útil para equipos pequeños.
**Plan**: gratis.
**Config**: `@modelcontextprotocol/server-slack`
**⚠️**: misma regla que email — read-only hasta confiar.

### filesystem · Acceso a sistema de archivos local

**Para qué**: explorar carpetas fuera del repo actual de forma controlada.
**Cuándo activarlo**: solo si necesitas Claude vaya a otra carpeta sin abrir nueva sesión.
**Config**: `@modelcontextprotocol/server-filesystem` con paths whitelisted.
**⚠️**: riesgo de seguridad. Whitelist específica obligatoria.

---

## 📊 Datos y canales para agencias (pilar Resultados/Entrega)

Estos MCPs alimentan con datos REALES los informes del pilar 4 y conectan canales del pilar 3. Patrón general: **conectar, no instalar** — casi todos son remotos u oficiales del vendor.

### google-meta-ads-ga4 · Todo-en-uno de paid + analytics
**Para qué**: Google Ads + Meta Ads + GA4 en un solo MCP ([irinabuht12-oss/google-meta-ads-ga4-mcp](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp), MIT). La base del informe mensual con datos de verdad.
**Coste**: gratis (OAuth con las cuentas del cliente).

### mcp-gsc · Search Console
**Para qué**: datos de búsqueda orgánica para los informes SEO ([AminForou/mcp-gsc](https://github.com/AminForou/mcp-gsc), MIT).
**Coste**: gratis.

### clarity · Heatmaps y session recordings (Microsoft, oficial)
**Para qué**: enseñarle al dueño del negocio "así usa la gente tu web". [microsoft/clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server).
**Coste**: gratis. **Límite**: API con pocas peticiones/día — para insights puntuales, no dashboard continuo.

### dataforseo · Reputación multi-portal + benchmarks locales (oficial)
**Para qué**: reseñas de Google/Trustpilot/TripAdvisor y datos de competencia local sin scraping ([dataforseo/mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript), Apache-2.0).
**Coste**: prepago por uso (céntimos por consulta) — enseñar control de gasto.

### elevenlabs · Voz en castellano (oficial)
**Para qué**: locuciones ES/LATAM para vídeos y reels ([elevenlabs/elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp), MIT).
**Coste**: free ~10 min/mes; Starter $5/mes.

### vapi / retell · Agentes telefónicos de voz (oficiales)
**Para qué**: recepcionista IA que atiende llamadas del negocio. Vapi: skills + MCP oficial ([VapiAI/skills](https://github.com/VapiAI/skills)). Retell: MCP alojado, buen soporte de español.
**Coste**: ~$0,10-0,20/min + número ~$2-3/mes. El coste lo paga el cliente final.

### resend · Email transaccional (oficial)
**Para qué**: confirmaciones y recordatorios enviados por agentes ([resend/resend-mcp](https://github.com/resend/resend-mcp), MIT).
**Coste**: gratis 3.000 emails/mes; requiere dominio verificado (Claude guía el DNS).

### hubspot · CRM remoto (oficial)
**Para qué**: para clientes que no están en GHL; MCP remoto `mcp.hubspot.com` con OAuth, cero instalación.
**Coste**: tier gratuito de HubSpot. (Pipedrive, Brevo, ActiveCampaign y MailerLite también tienen MCP remoto oficial.)

### google-news-trends · Tendencias por geografía
**Para qué**: "qué se busca ahora en tu zona" para propuestas y contenido ([jmanek/google-news-trends-mcp](https://github.com/jmanek/google-news-trends-mcp), MIT).
**Coste**: gratis, sin API key (basado en RSS: puede romperse si Google cambia).

---

## ⚠️ MCPs que evitar (en producción)

### Cualquier MCP que dé write a redes sociales sin gates

LinkedIn, Twitter, Instagram, Facebook auto-post: **alto riesgo de fuga de identidad**. Mejor: skill que prepara el draft y operador hace post manualmente.

### MCPs que no documentan claramente sus scopes

Si la documentación no especifica qué permisos pide y qué hace, no instalar.

### MCPs custom de developers desconocidos

`/install-mcp custom <url>` solo si confías en el dev o validas el código manualmente.

---

## Pattern para tu propio MCP curated list

Si trabajas con clientes que tienen stacks específicos, mantén tu propio `mcps-curated.md` por cliente en `clients/<nombre>/docs/mcps-curated.md`.

Estructura recomendada por entrada:
1. Nombre + tagline
2. Para qué sirve (1-2 frases)
3. Cuándo activarlo (caso de uso)
4. Riesgo de tokens (bajo/medio/alto)
5. Plan / coste
6. Config (`.mcp.json` snippet)
7. Variables (`.env`)
8. ⚠️ Notas de seguridad si aplica

---

## Token budget consideration

Cada MCP server activo en `.mcp.json` añade contexto al system prompt al iniciar Claude Code (las descripciones de sus tools). Más MCPs = más tokens base.

**Regla práctica**: 5-7 MCPs activos máximo. Si necesitas más, considera comentar los que no usas frecuentemente.

**Pro tip**: tener un `.mcp.json` por cliente (en `clients/<nombre>/.mcp.json` si Claude Code lo soporta) o cambiar `.mcp.json` antes de cada sesión según necesidad.

---

## Cómo añadir nuevos MCPs a esta lista

Para incluir un MCP en la curated list (PR al repo):

1. Probar el MCP en producción mínimo 2 semanas
2. Documentar:
   - Casos donde aporta valor real
   - Casos donde NO aporta (o es contraproducente)
   - Riesgos identificados
3. Submit PR con la entrada nueva siguiendo el formato de las top 5

Las contribuciones deben venir con experiencia real, no "instalé y parece OK".
