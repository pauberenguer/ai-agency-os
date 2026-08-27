# Plantillas de entregable — la marca de la casa

Tres plantillas HTML con la estética del OS (monocromo, una página, lenguaje de dueño de negocio). Las usan los playbooks `/informe`, `/auditoria` y `/propuesta`, y cualquier skill que genere entregables (vía `tool-visual-explainer`).

**Cómo se usan**: copiar la plantilla, incrustar `base.css` dentro de `<style>`, sustituir TODOS los `{{...}}` (el gate de entregables detecta los que se queden sin rellenar), guardar en `clients/<cliente>/entregables/YYYY-MM-nombre.html`.

**Personalización de agencia**: el operador puede cambiar `base.css` (su color de acento, su logo en el footer) UNA vez y toda su producción sale con su marca.
