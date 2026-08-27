#!/bin/bash
# ============================================================
#  AI Agency OS — add-client.sh
#  Crea cliente nuevo en clients/<nombre>/ desde un template vertical
#  Uso: bash scripts/add-client.sh <nombre-cliente> [vertical]
#       bash scripts/add-client.sh acme-corp freelance-ia
#       bash scripts/add-client.sh widget-shop agencia-marketing
# ============================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m'
BOLD='\033[1m'

# Paths
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CLIENTS_DIR="$REPO_ROOT/clients"
TEMPLATES_DIR="$CLIENTS_DIR/_templates"

# Validate args
CLIENT_NAME="${1:-}"
TEMPLATE="${2:-}"

if [ -z "$CLIENT_NAME" ]; then
    echo -e "${RED}ERROR${NC} Falta nombre del cliente"
    echo ""
    echo "Uso: bash scripts/add-client.sh <nombre-cliente> [vertical]"
    echo ""
    echo "Verticales disponibles:"
    if [ -d "$TEMPLATES_DIR" ]; then
        for t in "$TEMPLATES_DIR"/*/; do
            tname=$(basename "$t")
            [ "$tname" = "_templates" ] && continue
            echo "  - $tname"
        done
    fi
    echo "  - vacio (sin template, estructura mínima)"
    echo ""
    echo "Ejemplo: bash scripts/add-client.sh acme-corp freelance-ia"
    exit 1
fi

# Sanitize client name (kebab-case only)
if [[ ! "$CLIENT_NAME" =~ ^[a-z0-9-]+$ ]]; then
    echo -e "${RED}ERROR${NC} Nombre del cliente solo permite [a-z0-9-]"
    echo "       Convierte espacios a guiones: 'Acme Corp' → 'acme-corp'"
    exit 1
fi

CLIENT_DIR="$CLIENTS_DIR/$CLIENT_NAME"

# Check if client already exists
if [ -d "$CLIENT_DIR" ]; then
    echo -e "${RED}ERROR${NC} El cliente '$CLIENT_NAME' ya existe en $CLIENT_DIR"
    exit 1
fi

# Resolve template
if [ -z "$TEMPLATE" ] || [ "$TEMPLATE" = "vacio" ]; then
    USE_TEMPLATE=false
    echo -e "${CYAN}Modo:${NC} estructura vacía (sin template)"
else
    TEMPLATE_DIR="$TEMPLATES_DIR/$TEMPLATE"
    if [ ! -d "$TEMPLATE_DIR" ]; then
        echo -e "${RED}ERROR${NC} Template '$TEMPLATE' no existe en $TEMPLATES_DIR"
        echo ""
        echo "Verticales disponibles:"
        for t in "$TEMPLATES_DIR"/*/; do
            tname=$(basename "$t")
            [ "$tname" = "_templates" ] && continue
            echo "  - $tname"
        done
        exit 1
    fi
    USE_TEMPLATE=true
    echo -e "${CYAN}Modo:${NC} clonar desde template '$TEMPLATE'"
fi

echo ""
echo -e "${BLUE}Creando cliente '$CLIENT_NAME'...${NC}"

# Step 1: Create base structure
mkdir -p "$CLIENT_DIR"/{brand-context/{voice,positioning,icp,assets},context,projects/briefs,entregables,knowledge}

# Step 2: Copy template if applicable
if $USE_TEMPLATE; then
    # Copy brand-context templates
    cp "$TEMPLATE_DIR/brand-context/voice/voice-profile.template.md" "$CLIENT_DIR/brand-context/voice/voice-profile.md"
    cp "$TEMPLATE_DIR/brand-context/positioning/positioning.template.md" "$CLIENT_DIR/brand-context/positioning/positioning.md"
    cp "$TEMPLATE_DIR/brand-context/icp/icp.template.md" "$CLIENT_DIR/brand-context/icp/icp.md"

    # Copy context
    cp "$TEMPLATE_DIR/context/soul.md" "$CLIENT_DIR/context/soul.md"
    cp "$TEMPLATE_DIR/context/user.template.md" "$CLIENT_DIR/context/user.md"

    # Replace {{CLIENT_NAME}} placeholder in copied files
    if command -v sed &> /dev/null; then
        find "$CLIENT_DIR" -type f -name "*.md" -exec sed -i.bak "s/{{CLIENT_NAME}}/$CLIENT_NAME/g" {} \;
        find "$CLIENT_DIR" -name "*.bak" -delete
    fi

    # Knowledge pack del vertical (benchmarks, jerga, estacionalidad del sector)
    if [ -d "$TEMPLATE_DIR/knowledge" ]; then
        cp -R "$TEMPLATE_DIR/knowledge/." "$CLIENT_DIR/knowledge/"
        echo -e "${GREEN}  OK${NC} Knowledge pack del vertical copiado"
    fi

    echo -e "${GREEN}  OK${NC} Template '$TEMPLATE' clonado"
    echo -e "${CYAN}  ->${NC} Recuerda completar los placeholders {{...}} en:"
    echo -e "       $CLIENT_DIR/brand-context/voice/voice-profile.md"
    echo -e "       $CLIENT_DIR/brand-context/positioning/positioning.md"
    echo -e "       $CLIENT_DIR/brand-context/icp/icp.md"
    echo -e "       $CLIENT_DIR/context/user.md"
else
    # Modo vacío: solo .gitkeep en cada subcarpeta
    for d in brand-context/voice brand-context/positioning brand-context/icp brand-context/assets context projects projects/briefs; do
        touch "$CLIENT_DIR/$d/.gitkeep"
    done
    echo -e "${GREEN}  OK${NC} Estructura vacía creada"
    echo -e "${CYAN}  ->${NC} Configura el cliente con:"
    echo -e "       cd clients/$CLIENT_NAME && claude"
    echo -e "       Y ejecuta: /start-here (lanzará marketing-brand-voice si no hay voice profile)"
fi

# Step 3: Optional client-specific CLAUDE.md (override del raíz)
cat > "$CLIENT_DIR/CLAUDE.md" <<EOF
# CLAUDE.md — Cliente $CLIENT_NAME

> Al trabajar en esta carpeta, Claude ES la agencia de $CLIENT_NAME.
> El CLAUDE.md raíz del repo se sigue aplicando; este se merge encima.

## Cliente
- Nombre: $CLIENT_NAME
- Template base: ${TEMPLATE:-vacio}
- Creado: $(date -u +%Y-%m-%d)

## Al entrar aquí (SIEMPRE, antes de producir nada)

1. Lee \`brand-context/\` completo: voz (voice-profile.md), ICP (icp.md), posicionamiento (positioning.md). La voz del cliente manda sobre cualquier estilo por defecto.
2. Si existe \`knowledge/\`, es el conocimiento del sector de este cliente (benchmarks, jerga, estacionalidad): úsalo para dar contexto real a datos y propuestas.
3. Revisa el último entregable en \`entregables/\` — todo trabajo continúa una historia, no empieza de cero.

## Reglas de trabajo para este cliente

- Todo lo que vaya a ver el cliente se guarda en \`entregables/\` (con fecha: \`YYYY-MM-nombre\`), y pasa antes por tool-humanizer + tool-output-verifier o el subagente \`revisor\`.
- Números siempre con contexto y en impacto de negocio, no en métricas crudas.
- Idioma: castellano del mercado del cliente. Cero jerga de marketing sin explicar.
- Nunca inventar datos del cliente ni de su competencia: lo no verificado se marca \`[pendiente de confirmar]\`.

## Reglas específicas de $CLIENT_NAME

(Añade aquí lo que aplique SOLO a este cliente: temas vetados, competidores que no nombrar, tono en canales concretos…)

## Skills y playbooks más usados aquí

- \`/informe $CLIENT_NAME\` — informe mensual · \`/contenido $CLIENT_NAME\` — mes de redes
- (añade las skills que este cliente use recurrentemente)

## Notas operativas

(Lo que el operador deba recordar al trabajar aquí: accesos, horarios del dueño, particularidades)
EOF

echo -e "${GREEN}  OK${NC} CLAUDE.md del cliente creado"

# Done
echo ""
echo -e "${GREEN}${BOLD}============================================================${NC}"
echo -e "${GREEN}${BOLD}  Cliente '$CLIENT_NAME' creado correctamente${NC}"
echo -e "${GREEN}${BOLD}============================================================${NC}"
echo ""
echo -e "  ${BOLD}Estructura:${NC}"
echo -e "  $CLIENT_DIR/"
echo -e "  ├── CLAUDE.md (overrides cliente)"
echo -e "  ├── brand-context/"
echo -e "  │   ├── voice/voice-profile.md"
echo -e "  │   ├── positioning/positioning.md"
echo -e "  │   ├── icp/icp.md"
echo -e "  │   └── assets/"
echo -e "  ├── context/"
echo -e "  │   ├── soul.md"
echo -e "  │   └── user.md"
echo -e "  └── projects/"
echo ""
echo -e "  ${BOLD}Siguiente paso:${NC}"
echo -e "  ${CYAN}cd clients/$CLIENT_NAME && claude${NC}"
echo -e "  Y ejecuta ${CYAN}/start-here${NC} para arrancar la sesión con este cliente"
echo ""
