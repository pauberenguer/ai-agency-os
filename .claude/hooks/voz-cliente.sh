#!/bin/bash
# AI Agency OS — Guardia de voz (PreToolUse Write|Edit)
# Al escribir contenido en la carpeta de un cliente con brand-context,
# recuerda cargar su voz — una sola vez por sesión y cliente.
# Best-effort: nunca bloquea, siempre exit 0.
INPUT=$(cat)
python3 - "$INPUT" <<'PY' 2>/dev/null
import json, sys, os, re, hashlib, tempfile
try:
    data = json.loads(sys.argv[1])
except Exception:
    sys.exit(0)
fp = (data.get("tool_input") or {}).get("file_path", "")
norm = fp.replace("\\", "/")
m = re.search(r"(?:^|/)clients/([^/]+)/", norm)
if not m:
    sys.exit(0)
client = m.group(1)
if client.startswith("_"):
    sys.exit(0)
if not norm.lower().endswith((".md", ".html", ".txt")):
    sys.exit(0)
root = norm.split("/clients/")[0] if "/clients/" in norm else "."
bc = os.path.join(root, "clients", client, "brand-context")
if not os.path.isdir(bc):
    sys.exit(0)
sid = str(data.get("session_id", "nosession"))
marker = os.path.join(tempfile.gettempdir(),
                      "aaos-voz-" + hashlib.md5((sid + client).encode()).hexdigest()[:12])
if os.path.exists(marker):
    sys.exit(0)
open(marker, "w").write("1")
print(json.dumps({"systemMessage":
    f"🎙 Estás escribiendo para el cliente «{client}». Si aún no lo has hecho en esta sesión, "
    f"carga clients/{client}/brand-context/ (voz, ICP, posicionamiento) antes de redactar."}))
PY
exit 0
