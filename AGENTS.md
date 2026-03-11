# AGENTS.md — Máster 3D Integral Landing

Guía para mantener el estilo y la coherencia al añadir o modificar secciones de la landing. Usar este documento como referencia al crear contenido nuevo o al pedir cambios a un agente/IA.

---

## 1. Visión del proyecto

- **Producto:** Landing page del Máster 3D Integral (formación para Technical Artists).
- **Estética:** Minimalista, editorial, inspirada en referencias como SUSO Digital. Limpio, con mucho espacio en blanco y acentos muy controlados.
- **Paleta:** Solo **3 colores** — blanco, negro, violeta (`#7c3aed` y escala violet-50 … violet-900). No usar verde ni rojo como acentos.
- **Sensación:** Profesional, serio, “premium”, sin ruido visual.

---

## 2. Requisitos del cliente (identidad, calidez, conversión)

Estos puntos reflejan el feedback del cliente. Toda nueva sección o rediseño debe tenerlos en cuenta.

**Importante — Copy de referencia:** El texto/copy que el cliente ha pasado (títulos de sección, perfiles, organización del programa, profesorado, metodología, etc.) **es el copy que se utiliza**. No hay que quitar ni reemplazar ese contenido escrito; es la base del mensaje. Las indicaciones siguientes se refieren a **complementar** con más 3D y calidez, no a eliminar el copy.

### 2.1 Identidad visual: "Más 3D, menos texto"

- **Objetivo:** Que la web se sienta más del sector 3D y con impacto visual, **sin quitar** el copy existente.
- **Impacto visual:** **Añadir** imágenes o vídeo que expliquen la transformación (hero, antes/después, reels), **junto** al texto, no en lugar de él.
- **Mundo 3D:** La web debe **respirar 3D por todos lados**: más renders, wireframes, interfaces de software 3D, arte procedural, referencias al pipeline (Houdini, motores). El copy se mantiene; se enriquece el contexto visual.
- **Refuerzo visual:** Donde encaje, **complementar** con vídeos del portfolio o imágenes de alta calidad (resultados, piezas de alumnos o del equipo), sin sustituir los bloques de texto que el cliente ha definido.

### 2.2 Conexión humana y calidez (transformación personal)

- **Problema:** El diseño puede percibirse "frío" o "demasiado formal". El producto no es solo técnica 3D, sino **transformación personal**.
- **Mostrar rostros:** Es **vital** incluir fotos reales de las personas detrás del proyecto (Adolfo, Marta, Jas, Andrés, Santiago) para generar confianza y conexión emocional. Evitar solo iniciales o avatares genéricos donde el equipo tenga protagonismo.
- **Suavizar el tono:** Mantener el estilo tecnológico que gusta, pero hacerlo más **amable** y cercano; evitar un tono corporativo rígido.
- **Tipografía y calidez:** Valorar tipografías más **cercanas** (redondeadas, humanistas) donde tenga sentido, para transmitir programa de acompañamiento humano y no solo "curso técnico" o software.

### 2.3 Elementos de conversión (la oferta)

- **Problema:** Faltan componentes claros para el cierre de la venta.
- **Cajetín de producto (The Stack):** Diseñar un **bloque claro** que muestre:
  - Opciones de compra / planes o paquetes.
  - Precios y formas de pago.
  - Qué incluye cada opción (listado escaneable).
- Este bloque debe ser fácil de localizar y de leer; es clave para la conversión.

### 2.4 Resumen operativo (para Johana y equipo)

- **Humanizar la interfaz:** Fotos reales de personas (equipo, alumnos, mentores) en secciones relevantes.
- **Saturar visualmente con 3D:** Renders, vídeos, mockups de software 3D, arte generativo; que el nicho se reconozca al instante.
- **Secciones reutilizables:** Cada sección debe poder **copiarse y pegarse** en otras páginas sin tocar una sola línea de código (bloques autocontenidos, sin dependencias rotas).

---

## 3. Sistema de diseño

### Colores
- **Fondo principal:** `bg-white` o `bg-gray-50` (alternar por sección para ritmo).
- **Texto:** `text-black` / `text-gray-500` (cuerpo), `text-gray-400` (secundario).
- **Acento:** `text-violet-600`, `bg-violet-100`, `border-violet-200`, etc. Violeta como único color de marca.
- **Contraste fuerte:** Bloques `bg-black text-white` para destacar (ej. una card central, banners, CTAs).
- **Gradiente de texto:** Clase `.gradient-text` (violeta suave) solo para **una o dos palabras** por título, no frases largas.

### Tipografía
- **Sans:** Inter (títulos y cuerpo). Pesos: `font-extrabold` títulos, `font-bold` subtítulos, `font-semibold` énfasis, `font-normal` cuerpo.
- **Mono:** JetBrains Mono (`font-mono`). Uso: etiquetas de sección, pills, datos técnicos, roles.
- **Tamaños:** Títulos de sección `text-5xl` / `text-6xl` con `leading-[1.0]` o `tracking-tight`. Cuerpo `text-base` o `text-sm`, descripciones secundarias `text-xs`.

### Espaciado
- **Secciones:** `py-28 lg:py-36` (padding vertical estándar).
- **Contenedor:** `max-w-7xl mx-auto px-6`.
- **Entre bloques dentro de sección:** `mb-20` o `mb-16` para separar título de contenido; `gap-8` o `gap-6` en grids.

### Bordes y sombras
- **Cards:** `rounded-2xl`, `border border-gray-100`. En hover: `hover:border-violet-200`, `hover:shadow-lg`.
- **Botones / pills:** `rounded-full` para CTAs y pills de navegación.
- **Evitar** bordes gruesos o colores llamativos; mantener líneas finas y grises suaves.

---

## 4. Estructura de una sección nueva

Toda sección debe:

1. Tener un **id** único y descriptivo (kebab-case) para enlaces de ancla y nav.
2. Usar la clase de sección estándar: `py-28 lg:py-36` y, si aplica, `bg-gray-50` o `bg-white` para alternar con la anterior.
3. Incluir un **encabezado** con:
   - **Label de sección:** `font-mono text-violet-600 text-xs uppercase tracking-[0.25em] mb-4`.
   - **Título:** `text-5xl` o `text-6xl font-extrabold tracking-tight`. Opcionalmente una palabra (o dos) con `gradient-text`.
   - **Subtítulo/descripción** (opcional): `text-gray-500 text-base` o `text-lg`, `max-w-xl` o `max-w-2xl` si está centrado.

### Patrones de header por tipo de sección

- **Centrado (clásico):**  
  `text-center mb-20` → label + título + párrafo intro.

- **Editorial (dos columnas):**  
  `flex flex-col lg:flex-row lg:items-end lg:justify-between gap-8 mb-20` → título a la izquierda, texto corto o resumen a la derecha (p. ej. “Para Quién Es”, “Organización”, “Profesorado”).

---

## 5. Componentes reutilizables

### Card estándar (con hover)
```html
<div class="card-hover rounded-2xl border border-gray-100 p-8 bg-white">
  <!-- contenido -->
</div>
```
- Para listas de ítems (perfiles, habilidades, días de la semana): usar grid (`grid-cols-1 md:grid-cols-2` o `lg:grid-cols-3/4`) y esta card.
- Opcional: barra superior animada en hover con `absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-violet-600 to-violet-300` y `group-hover:scale-x-100`.

### Card destacada (fondo negro)
- Una card del grid puede ser `bg-black text-white` para dar jerarquía (ej. Eje Y en “3 Ejes”, días Martes/Jueves en Organización).
- En negro: texto `text-gray-300`/`text-gray-400`, labels `text-violet-400`, bordes `border-violet-500/20`.

### Pills / tags
- `font-mono text-xs px-4 py-2 rounded-full bg-white border border-gray-200` (o `bg-violet-100` si es etiqueta de categoría). Para acento: `text-violet-600` o `strong` en violeta.

### Listas con icono
- Ítem: `flex items-center gap-3` o `gap-2`, con `w-5 h-5 rounded-full bg-violet-100 text-violet-600` + check o bullet, y texto `font-mono text-sm text-gray-600`.

### Botones
- **Primario:** `bg-black text-white px-8 py-4 rounded-full font-semibold text-sm hover:bg-violet-600 transition-colors tracking-wide`.
- **Secundario:** `border border-gray-200 text-gray-700 ... rounded-full hover:border-violet-600 hover:text-violet-600`.

### Banner final de sección (CTA)
- Contenedor: `rounded-2xl bg-black text-white overflow-hidden`, padding generoso (`p-10`).
- Label: `font-mono text-violet-400 text-xs uppercase tracking-[0.2em]`.
- Título: `text-2xl` o `text-3xl font-extrabold`.
- Texto: `text-gray-300`/`text-gray-400` `text-sm`. Opcional: botón `bg-white text-black ... rounded-full` alineado a la derecha (flex).

---

## 6. Secciones actuales y sus IDs

| ID (ancla)   | Nombre / contenido breve                    |
|--------------|---------------------------------------------|
| `#programa`  | Propuesta de valor — 3 Ejes                 |
| `#para-quien`| Este Máster es para ti si… (4 perfiles)     |
| `#testimonios` | Caso de éxito (testimonio)                |
| `#arsenal`   | Arsenal del Artista 3D (habilidades)         |
| `#organizacion` | Tu transformación, paso a paso (calendario, horarios, metodología) |
| `#mentoria`  | Mentoría personalizada                       |
| `#profesorado` | Equipo principal + profesores 3D           |
| `#cta`       | CTA final “¿Listo para el cambio?”          |

Al añadir una sección nueva:
- Crear `id="kebab-case"` único.
- Añadir enlace en la nav con `href="#nuevo-id"` y clase `nav-link`.

---

## 7. Contenido y tono

- **Voz:** Directa, segura, orientada a resultados profesionales; pero **amable** y cercana (ver §2.2). Evitar exceso de adjetivos o promesas vagas, y un tono excesivamente formal o frío.
- **Ejes del máster:** Siempre nombrar con mayúsculas cuando sea etiqueta (EJE X, EJE Y, EJE Z) y asociar: X = Formación 3D / Capacitación; Y = Orden interno / Mentalidad; Z = Negocio / Marca / Freelance.
- **Testimonios:** Texto del quote más corto que el resto del copy; priorizar que se vea bien la cara o el contexto visual.
- **Profesorado:** Destacar una persona (ej. Adolfo) con bloque ancho o full-width; el resto en grid de cards compactas con rol + Eje en `font-mono` y bio breve. **Incluir fotos reales** del equipo (Adolfo, Marta, Jas, Andrés, Santiago) para conexión humana (§2.2).

---

## 8. Añadir una sección nueva (checklist)

1. Definir **id** y **título** de sección.
2. Elegir **fondo:** `bg-white` o `bg-gray-50` según la sección anterior.
3. Usar **header** editorial o centrado según el tipo de contenido.
4. Reutilizar **cards**, **pills** y **botones** del sistema; no inventar nuevos estilos de card/botón sin motivo.
5. Mantener **espaciado** (`py-28 lg:py-36`, `mb-20`, `gap-6`/`gap-8`).
6. Añadir enlace en la **nav** con clase `nav-link` y `href="#id-de-la-seccion"`.
7. Si la sección es larga, considerar un **banner/CTA** al final (negro, con o sin botón).
8. **Requisitos cliente (§2):** Usar el **copy que el cliente ha pasado** (no quitarlo). **Complementar** con imagen o vídeo y **elementos 3D** (renders, UI, arte) donde encaje; usar **fotos reales** si la sección habla de personas; mantener tono **amable**; si es la oferta, incluir bloque claro de **precios/planes/formas de pago** (The Stack). La sección debe ser **autocontenida** para poder copiar/pegar en otras páginas.

---

## 9. Assets y técnico

- **Fuentes:** Inter, JetBrains Mono, Material Symbols Outlined (Google Fonts).
- **Estilos:** Tailwind vía CDN; configuración en `<script>` en `index.html` (colores violet, fontFamily).
- **Clases globales** definidas en `<style>`: `.gradient-text`, `.card-hover`, `.nav-link`, `.blob-*`, `.float-anim`, `.cursor-anim`, `.badge-float-*`, `.fade-in`, etc. Reutilizar antes de crear nuevas clases inline.
- **Imágenes:** Hero usa `hero-3d.png`; resto pueden ser URLs externas (ej. Unsplash) o assets locales. Mantener `alt` descriptivo y tamaños coherentes (evitar imágenes enormes sin necesidad).

---

## 10. Lo que no hacer

- No introducir **verde** ni **rojo** como color de acento.
- No usar **más de una palabra** (o dos) con `gradient-text` por título.
- No saturar de animaciones: las que hay (blobs, cursor, badges flotantes) están en el hero; en secciones nuevas preferir transiciones suaves (hover) en lugar de animaciones continuas.
- No cambiar la paleta a 4+ colores; mantener **blanco, negro, violeta**.
- No olvidar el **id** de sección ni el **enlace en la nav** al crear contenido nuevo.

---

Con esto, cualquier agente o desarrollador puede mantener el mismo estilo en nuevas secciones y actualizaciones de la landing del Máster 3D Integral.
