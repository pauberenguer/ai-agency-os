---
name: automation-whatsapp-agent
description: "Construye un agente de WhatsApp con IA para un negocio (propio o de un cliente) en menos de 30 minutos, sin programar. Usa el kit AgentKit: Claude Code entrevista al usuario, genera el agente completo (servidor, cerebro Claude, memoria por cliente, herramientas del negocio), lo prueba en un simulador de terminal y lo despliega a producción vía Railway. USAR cuando el usuario diga 'agente de WhatsApp', 'bot de WhatsApp', 'automatizar WhatsApp', 'responder clientes por WhatsApp', 'chatbot para mi negocio/cliente', o quiera vender automatización de atención al cliente."
version: "1.0.0"
---

# Agente de WhatsApp con IA (AgentKit)

## Qué entrega

Un agente de WhatsApp funcionando en producción para un negocio: responde a
clientes 24/7 con la personalidad y los datos del negocio (menú, precios,
horarios, FAQ), recuerda el historial de cada cliente y escala a humano cuando
no sabe algo. Es un **entregable vendible** para clientes de agencia.

## Cuándo usar esta skill

- El operador quiere ofrecer automatización de WhatsApp como servicio.
- Un cliente pide atención automática por WhatsApp.
- El operador quiere el agente para su propio negocio.

## Cuándo NO usarla

- El cliente ya tiene un CRM con automatización de WhatsApp (p. ej. GoHighLevel
  con WhatsApp conectado): valorar primero si la automatización nativa del CRM
  cubre el caso — menos piezas móviles.
- Solo se necesita un autoresponder simple (mensaje de ausencia): sobra un agente.

## Requisitos (verificar ANTES de arrancar)

1. **Python 3.11+** (`python3 --version`)
2. **API key de Anthropic** (`sk-ant-...`) — cuenta de API, separada de la suscripción
3. **Cuenta de WhatsApp API**: [Zernio](https://zernio.com) (recomendado, resuelve
   la conexión) o [Meta Cloud API](https://developers.facebook.com) (directo, más pasos)
4. Para producción: cuenta de GitHub + [Railway](https://railway.app)

## Procedimiento

1. **Ubicación**: si es para un cliente, trabajar en `clients/<nombre>/projects/whatsapp-agent/`.
   Si es propio, `projects/whatsapp-agent/`.
2. **Clonar el kit**:
   ```bash
   git clone https://github.com/Hainrixz/whatsapp-agentkit.git <destino>
   cd <destino> && bash start.sh
   ```
3. **Construir**: abrir Claude Code en esa carpeta y ejecutar `/build-agent`.
   El kit guía cinco fases: entorno → entrevista (10 preguntas del negocio) →
   generación del agente → prueba en simulador local → deploy a Railway.
4. **Datos del negocio**: preparar antes los archivos de conocimiento (menú,
   precios, políticas, FAQ) — van a `knowledge/` y el agente responde SOLO con eso.
5. **Prueba con el dueño**: antes de conectar el número real, sesión de prueba
   en el simulador con el cliente presente. Ajustar tono y respuestas ahí.
6. **Registro**: al terminar, anotar en el decisions-log del cliente qué se
   desplegó, con qué proveedor de WhatsApp y dónde viven las claves.

## Reglas

- Las API keys van SOLO en `.env` del proyecto del kit — nunca en el repo del OS.
- El agente no inventa datos: si el negocio no ha dado la información, la respuesta
  correcta es "no lo sé, te paso con una persona". Verificarlo en la fase de prueba.
- El coste de API del agente lo paga el cliente final — dejarlo claro en la propuesta.

## Skills relacionadas

- **`automation-n8n-builder`** — si el flujo necesita integraciones más allá de
  la conversación (CRM, hojas de cálculo, calendarios).
- **`tool-output-verifier`** — pasar los prompts del agente por el quality gate
  antes de entregar al cliente.
