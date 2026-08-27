#!/bin/bash
# ============================================================
#  AI Agency OS — _debrand-engine.sh
#
#  El engine vendored (vendor/sinapsis/) instala sus artefactos en
#  ~/.claude/ con su propia nomenclatura. Este script renombra las
#  COPIAS instaladas a la nomenclatura AI Agency OS. vendor/ queda
#  intacto, así /actualiza sigue pudiendo traer upstream.
#
#  Idempotente: re-ejecutar = no-op. Lo llaman install.sh (tras el
#  installer vendored) y update.sh (antes de re-cablear hooks).
#  También se puede ejecutar suelto: bash scripts/_debrand-engine.sh
#
#  Los datos aprendidos viven en ~/.claude/homunculus/ y en los
#  _*.json de la raíz de skills/: ninguno se borra aquí. Las carpetas
#  de skills del engine son solo código → seguras de reemplazar.
# ============================================================
set -uo pipefail

CLAUDE_HOME="${1:-$HOME/.claude}"
SKILLS_DIR="$CLAUDE_HOME/skills"
CMDS_DIR="$CLAUDE_HOME/commands"

[ -d "$SKILLS_DIR" ] || exit 0

# 1) Carpetas de skills del engine (código, sin datos)
for pair in "sinapsis-learning:agency-learning" "sinapsis-instincts:agency-instincts"; do
    src="${pair%%:*}"; dst="${pair##*:}"
    if [ -d "$SKILLS_DIR/$src" ]; then
        rm -rf "$SKILLS_DIR/$dst"
        mv "$SKILLS_DIR/$src" "$SKILLS_DIR/$dst"
    fi
done

# 2) Registro de proyectos (data file: preservar el que ya tenga datos)
if [ -f "$SKILLS_DIR/_sinapsis-projects.json" ]; then
    if [ -f "$SKILLS_DIR/_agency-projects.json" ]; then
        # el installer re-creó el template porque no vio el suyo → es un blank
        rm -f "$SKILLS_DIR/_sinapsis-projects.json"
    else
        mv "$SKILLS_DIR/_sinapsis-projects.json" "$SKILLS_DIR/_agency-projects.json"
    fi
fi

# 3) Comando global con marca en el nombre
if [ -f "$CMDS_DIR/dashboard-sinapsis.md" ]; then
    mv -f "$CMDS_DIR/dashboard-sinapsis.md" "$CMDS_DIR/dashboard-agency.md"
fi

# 4) Referencias internas en las copias instaladas.
#    perl -i preserva permisos (los data files van chmod 600).
targets=()
for f in "$SKILLS_DIR"/_*.sh "$SKILLS_DIR"/_*.json "$SKILLS_DIR"/_*.py \
         "$SKILLS_DIR"/_*.html "$CLAUDE_HOME/CLAUDE.md" \
         "$CLAUDE_HOME/settings.json" "$CMDS_DIR"/*.md; do
    [ -f "$f" ] && targets+=("$f")
done
while IFS= read -r -d '' f; do
    targets+=("$f")
done < <(find "$SKILLS_DIR/agency-learning" "$SKILLS_DIR/agency-instincts" \
              "$SKILLS_DIR/skill-router" -type f -print0 2>/dev/null)

for f in "${targets[@]}"; do
    perl -pi -e '
        s{github\.com/Luispitik/sinapsis}{github.com/pauberenguer/ai-agency-os}g;
        s/dashboard-sinapsis/dashboard-agency/g;
        s/sinapsis-learning/agency-learning/g;
        s/sinapsis-instincts/agency-instincts/g;
        s/_sinapsis-projects/_agency-projects/g;
        s/Sinapsis/AI Agency OS/g;
        s/SINAPSIS/AI AGENCY OS/g;
        s/sinapsis/ai-agency-os/g;
    ' "$f" 2>/dev/null || true
done

exit 0
