---
name: discovery-call-prep
description: Prepara una reunión de discovery con un cliente potencial. Genera preguntas específicas según el contexto del cliente y el servicio ofrecido, propone agenda de 45 minutos y redacta el mensaje de confirmación previo a la reunión. Activa este skill cuando el usuario diga "voy a tener una reunión con un cliente", "me contactó un cliente potencial", "necesito preparar una discovery call", "cómo me preparo para una reunión de ventas", o cuando el usuario comparta el correo o mensaje inicial de un cliente potencial.
---

# Discovery Call Prep

## Cuándo activar

Cuando el usuario expresa que va a tener una primera reunión con un cliente potencial y necesita prepararse. Los triggers explícitos incluyen frases como "reunión con cliente", "discovery call", "primer contacto cliente", "me escribió alguien interesado", "cómo me preparo para vender".

## Qué hace este skill

Analiza el contexto del cliente y del servicio del usuario, y genera cuatro entregables:

1. **Investigación previa recomendada**: qué debe buscar el usuario sobre el cliente y su empresa antes de la reunión (15 a 30 minutos de research).

2. **Preguntas de discovery obligatorias**: 8 a 12 preguntas específicas al contexto que permiten entender el problema real, el volumen, las herramientas actuales, el presupuesto y el criterio de éxito.

3. **Agenda de 45 minutos**: dividida en rapport, discovery, contexto del freelancer, aproximación técnica, y next steps. Con tiempos exactos por sección.

4. **Mensaje de confirmación previo a la reunión**: para enviar al cliente 24 horas antes, confirmando hora, agenda breve y pidiendo material que le sirva al usuario (screenshots, ejemplos, acceso).

## Cómo activarlo

El usuario debe compartir mínimamente:

- Contexto del cliente (empresa, industria, tamaño aproximado si sabe)
- Qué servicio o solución está pensando ofrecer
- Fecha y hora tentativa de la reunión (opcional)

Si el usuario ya recibió un correo o mensaje inicial del cliente, pedirle que lo comparta completo. Ese texto es la mejor materia prima para inferir el contexto real.

## Reglas duras que aplica el skill

- Cero preguntas genéricas tipo "cuéntame sobre tu empresa". Todas las preguntas deben ser específicas al contexto compartido.
- La agenda nunca cierra precio en vivo. Siempre propone enviar propuesta escrita en 3 días hábiles.
- Recomienda grabar la reunión con permiso.
- Recomienda escuchar 70% y hablar 30%.
- Sugiere pedir al menos una screenshot o acceso al proceso actual del cliente.

## Formato de salida

Cuatro secciones claramente separadas con títulos:

```
RESEARCH PREVIO (15 a 30 min antes de la reunión)
- Item 1
- Item 2
...

PREGUNTAS DE DISCOVERY (8 a 12 preguntas)
1. Pregunta específica sobre volumen
2. Pregunta específica sobre herramientas actuales
...

AGENDA DE 45 MINUTOS
- Rapport (5 min): [detalle]
- Discovery (20 min): [detalle]
- Contexto tuyo (5 min): [detalle]
- Aproximación técnica (10 min): [detalle]
- Next steps (5 min): [detalle]

MENSAJE DE CONFIRMACIÓN PREVIA
Texto listo para copiar y pegar, dirigido al cliente.
```

## Notas para el usuario

Después de la reunión, el próximo paso natural es activar el skill `proposal-writer` para redactar la propuesta escrita con las notas de discovery como input.
