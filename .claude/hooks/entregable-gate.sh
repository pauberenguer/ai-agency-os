#!/bin/bash
# AI Agency OS — Gate de entregables (PostToolUse Write|Edit)
# Si el archivo escrito es material de cliente (clients/**/*.md|html|txt),
# lo escanea en busca de señales de "no enviable" y avisa vía systemMessage.
# Best-effort: nunca bloquea, siempre exit 0.
INPUT=$(cat)
python3 - "$INPUT" <<'PY' 2>/dev/null
import json, sys, re, os
try:
    data = json.loads(sys.argv[1])
except Exception:
    sys.exit(0)
fp = (data.get("tool_input") or {}).get("file_path", "")
norm = fp.replace("\\", "/")
if "/clients/" not in norm and not norm.startswith("clients/"):
    sys.exit(0)
if "/_templates/" in norm:
    sys.exit(0)
if not norm.lower().endswith((".md", ".html", ".txt")):
    sys.exit(0)
try:
    s = open(fp, encoding="utf-8", errors="replace").read()
except Exception:
    sys.exit(0)
issues = []
for pat, msg in [
    (r"\[PERSONALIZA[^\]]*\]", "placeholders sin rellenar"),
    (r"\bTODO\b|\bXXX\b|\bTBD\b", "marcadores TODO/XXX/TBD"),
    (r"\{\{[^}]+\}\}", "variables {{...}} sin sustituir"),
    (r"[Ll]orem ipsum", "texto de relleno lorem ipsum"),
    (r"[Cc]omo (una )?IA\b|As an AI", "frases de asistente IA"),
    (r"[Ee]n el mundo actual|[Ee]n la era digital|In today'?s", "muletillas AI-tell"),
]:
    if re.search(pat, s):
        issues.append(msg)
if issues:
    print(json.dumps({"systemMessage":
        "⚠ Gate de entregables — «" + os.path.basename(fp) + "» contiene: " + ", ".join(issues) +
        ". Antes de darlo por entregado: corrígelo y pásalo por tool-humanizer + tool-output-verifier (o el subagente revisor)."}))
PY
exit 0
