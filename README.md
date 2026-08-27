<h1 align="center">AI Agency OS</h1>

<p align="center">
  <em>El sistema operativo de tu agencia de IA.<br>
  Memoria persistente, skills listas para usar y multi-cliente desde el día uno.</em>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://aiagencyaccelerator.com"><img src="https://img.shields.io/badge/by-AI%20Agency%20Accelerator-111.svg" alt="AI Agency Accelerator"></a>
</p>

---

## 🚀 Instalación

**Camino recomendado — sin terminal.** Clona el repo, abre Claude Code en la carpeta y escribe:

> **instala esto**

Claude ejecuta el instalador por ti, verifica que todo quedó bien y arranca tu onboarding. Funciona en Mac y Windows.

<details>
<summary>Camino manual (terminal)</summary>

```bash
git clone https://github.com/pauberenguer/ai-agency-os.git ~/ai-agency-os
cd ~/ai-agency-os
bash scripts/install.sh
```

En **Windows**, ejecútalo desde **Git Bash** (viene con [Git para Windows](https://git-scm.com/download/win)), no desde cmd/PowerShell.
</details>

Después de la parte técnica, el resto pasa dentro de Claude Code:

1. Al abrir sesión, el sistema detecta que falta el onboarding y te guía.
2. El asistente te entrevista ~10 minutos y rellena tu contexto (`context/`).
3. Al terminar, genera tu primer entregable real en unos 5 minutos.

Total realista: **15-20 minutos** y sales con el sistema funcionando.

**¿Algo falla?**

```bash
bash scripts/install.sh --resume           # continúa desde la última fase completada
bash scripts/install.sh --force-reinstall  # backup del estado y arranque limpio
```

Desde Claude Code, `/install-status` muestra el estado sin tocar nada.

## Qué es

AI Agency OS convierte una sesión vanilla de Claude Code en el puesto de trabajo de un operador de IA profesional. Tres capas:

1. **Engine de memoria** — contexto que persiste entre sesiones, aprendizaje de tus patrones de trabajo y skills que se activan cuando las necesitas (motor: Sinapsis, ver `vendor/`).
2. **Capa de negocio** — tu marca (voz, posicionamiento, ICP), tu contexto de trabajo, tus proyectos y tus clientes, cada uno con su espacio y sus templates por vertical.
3. **Catálogo 100** — exactamente 100 skills curadas en 5 pilares de 20: **Sistema** (tu OS y tu cabeza), **Clientes** (conseguir y cerrar), **Entrega** (los servicios que facturas), **Resultados** (demuestra lo que vales) y **Operaciones** (la agencia que no se rompe). Todas con licencia libre verificada (MIT/Apache) y convención única (`SKILL.md` + `ORIGIN.md` + `LICENSE`). Regla de la casa: el catálogo vive en 100 — para que entre una skill, sale la más débil de su pilar.

## Para quién

- Alumnos de [AI Agency Accelerator](https://aiagencyaccelerator.com) (audiencia principal)
- Operadores de IA que sirven a varios clientes
- Agencias pequeñas que quieren estandarizar su stack agéntico

No necesitas saber programar. Sí necesitas ~20 minutos de configuración guiada la primera vez.

## Qué te da el primer día

- ✅ Memoria entre sesiones: no vuelves a explicar tu negocio cada día
- ✅ Tu primer entregable real generado en los primeros 20 minutos
- ✅ Catálogo de 100 skills en 5 pilares, listo para activarse conversando
- ✅ Multi-cliente con templates por vertical para escalar
- ✅ Log de decisiones que mantiene a Claude coherente entre sesiones
- ✅ `/doctor` para diagnosticar y arreglar cualquier desviación

## 💰 Coste real

AI Agency OS es gratis. Claude no. Léelo antes de instalar:

| Concepto | Coste |
|---|---|
| AI Agency OS (este repo) | **Gratis** (MIT) |
| Claude Desktop / Claude Code | Gratis (descarga) |
| **Anthropic Pro** | **$20/mes** — el mínimo para que el OS funcione bien |
| Anthropic Max | $100-200/mes — para sesiones largas o uso intensivo |

Con el plan Free de Anthropic los modelos buenos no llegan y el sistema se siente roto. El mínimo realista es **Pro ($20/mes)**.

## Comandos principales

| Comando | Qué hace |
|---|---|
| `/start-here` | Abre sesión: carga contexto y prioridades |
| `/wrap-up` | Cierra sesión: guarda lo aprendido y deja el contexto listo |
| `/recuerda` | Guarda un dato, decisión o preferencia en memoria |
| `/add-client` | Da de alta un cliente con su espacio y template de vertical |
| `/skills` | Lista e instala skills de la biblioteca |
| `/doctor` | Diagnostica la instalación y propone arreglos |
| `/auditoria <web>` | Auditoría completa en paralelo (SEO+UX+legal+ads) con informe vendible |
| `/propuesta <prospecto>` | De prospecto a propuesta con ROI, lista para enviar |
| `/prospecta <zona> <sector>` | Encuentra negocios locales, prioriza y prepara los mensajes |
| `/informe <cliente>` | El informe mensual con datos reales — el ritual que renueva contratos |
| `/contenido <cliente>` | El mes de redes: calendario + piezas con la voz del cliente |
| `/actualiza` | Trae la última versión del OS sin pisar tu contexto |
| `/backup` · `/restaura` | Copia y restauración de tu memoria y contexto |

## Estructura

```
ai-agency-os/
├── context/          # Quién eres, en qué trabajas, prioridades
├── brand-context/    # Voz, posicionamiento, ICP de tu marca
├── clients/          # Un espacio por cliente + templates por vertical
├── projects/         # Proyectos estructurados
├── loops/            # Trabajo repetitivo convertido en sistema
├── skills-library/   # Catálogo 100 · 5 pilares de 20 skills
│   ├── 1-sistema/  2-clientes/  3-entrega/
│   ├── 4-resultados/  5-operaciones/
├── plantillas/       # Plantillas de entregable (informe, auditoría, propuesta)
├── .claude/          # Skills core, playbooks, subagentes, output styles y hooks
├── scripts/          # Instalador, backup, update, doctor
└── vendor/           # Componentes de terceros (ver CREDITS.md)
```

## Documentación

- [`docs/quickstart.md`](docs/quickstart.md) — primeros pasos tras instalar
- [`docs/installation.md`](docs/installation.md) — instalación en detalle y resolución de problemas
- [`docs/multi-client-guide.md`](docs/multi-client-guide.md) — cómo trabajar multi-cliente
- [`docs/skill-creation-guide.md`](docs/skill-creation-guide.md) — crea tus propias skills

## Licencia

MIT — ver [`LICENSE`](LICENSE). Este proyecto incorpora componentes de terceros bajo MIT; los avisos de copyright están en [`CREDITS.md`](CREDITS.md).
