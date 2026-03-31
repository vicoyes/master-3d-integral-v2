# Mapeo de clases CSS → Go High Level (Máster 3D Integral)

Documento de referencia: qué **clases** (sin punto) pegar en cada tipo de elemento.  
Requiere tener pegado el archivo **`gohighlevel-custom.css`** en el CSS personalizado de GHL.

Las clases usan el prefijo **`m3d-`**. Puedes combinar varias en el mismo campo, separadas por espacio.

---

## Animaciones (añadir junto al texto o bloque)

| Clase | Efecto |
|--------|--------|
| `m3d-fade-in` | Entrada suave desde abajo + opacidad (al cargar) |
| `m3d-fade-in-delay-1` | Igual, retardo corto (típico: segundo bloque) |
| `m3d-fade-in-delay-2` | Retardo medio |
| `m3d-fade-in-delay-3` | Retardo largo (último bloque del hero) |
| `m3d-float-anim` | Movimiento vertical muy suave en loop (vídeo / imagen hero) |
| `m3d-reveal` | Estado inicial “oculto” para revelar con JS (opcional) |
| `m3d-visible` | Se añade con script al elemento que ya tenía `m3d-reveal` |

**Ejemplo hero:** label → `m3d-label-gradient m3d-fade-in` · h1 → `m3d-heading-hero m3d-fade-in m3d-fade-in-delay-1` · párrafo → `m3d-text-body m3d-fade-in m3d-fade-in-delay-2`.

---

## Photos collage (collage de fotos + pastilla CTA)

Bloque de **`index.html`** comentado como `<!-- Photos Collage Section -->`: fondo con blobs animados, geometría SVG, cuatro fotos superpuestas y barra tipo píldora con avatares y botón “AGENDAR LLAMADA”.

**Fragmento completo:** `snippets/ghl-photos-collage.html` (no confundir con `snippets/ghl-para-quien.html`, que es otra sección). Las imágenes van con **URLs absolutas** (Unsplash vía API imgix `ixlib=…`) para que carguen dentro de GHL; si quieres las mismas fotos que en la landing (`1.12.png`, etc.), súbelas a Medios y sustituye cada `src`.

| Elemento | Clases (sin punto) |
|----------|-------------------|
| `<section>` | `m3d-collage-section` |
| Capa fondo (blobs + SVG) | `m3d-collage-bg` |
| Contenedor blobs centrados | `m3d-collage-blobs-wrap` + hijos `m3d-collage-blob m3d-collage-blob--a` … `--d` |
| SVG hexágono | `m3d-collage-geo` |
| Contenedor ancho + capas | `m3d-container` + `m3d-collage-inner` |
| Área de altura fija del collage | `m3d-collage-stage` |
| Marco foto 1–4 | `m3d-collage-frame m3d-collage-frame--1` … `--4` (`--4` solo desde `md`) |
| Fila pastilla CTA | `m3d-collage-pill-row` |
| Pastilla blanca | `m3d-collage-pill` |
| Avatares superpuestos | `m3d-collage-avatars` (imgs dentro) |
| Textos “+120…” / “Comunidad” | `m3d-collage-pill-copy` + `m3d-collage-pill-title` / `m3d-collage-pill-sub` (copy oculto en móvil muy estrecho) |
| Botón compacto | `m3d-btn m3d-btn-primary m3d-btn-sm` |

---

## Shell + halo degradado (bloque tipo “Para quién”)

Contenedor con **mancha de color difuminada** detrás (misma idea que `index.html`: capa absoluta + blur).

**Fragmento completo (copiar/pegar en GHL):** archivo del repo `snippets/ghl-para-quien.html` — incluye halo, card blanca, grid texto + imagen y el copy de “Para quién es”.

**Estructura HTML mínima**

```html
<div class="m3d-block-shell m3d-block-shell--spaced-top">
  <div class="m3d-gradient-glow" aria-hidden="true"></div>
  <div class="m3d-block-shell-front">
    <!-- aquí va la card o el grid (texto + imagen, etc.) -->
  </div>
</div>
```

| Elemento | Clases (sin punto) |
|----------|-------------------|
| **Contenedor padre** | `m3d-block-shell` — ancho máximo, centrado, padding horizontal, `position: relative` |
| Opcional: margen superior grande | `m3d-block-shell--spaced-top` — mismo ritmo que el bloque bajo el slider en la landing |
| **Capa del degradado** (vacía, solo decoración) | `m3d-gradient-glow` — debe ser **hijo directo** del shell, antes del contenido |
| **Wrapper del contenido** (card blanca, etc.) | `m3d-block-shell-front` — sube el contenido por encima del halo (`z-index`) |
| **Card blanca** interior | `m3d-shell-inner-card` |
| **Grid** dos columnas (texto \| imagen ≥1024px) | `m3d-split-pq` |
| Columna texto | `m3d-split-pq-copy` |
| Columna imagen | `m3d-split-pq-media` (la `img` va dentro) |
| Lista de perfiles | `m3d-pq-stack` envuelve ítems con `m3d-pq-item` |

Puedes añadir animación al shell: `m3d-block-shell m3d-reveal m3d-visible` (si usas JS) o `m3d-fade-in`.

---

## Barra superior (webinar)

| Elemento | Clases sugeridas |
|----------|------------------|
| Fila / barra | (estilo inline GHL: fondo negro, texto blanco) o clase propia si la creas |
| Texto pequeño | `font-mono` en GHL + tamaño xs; color blanco |
| Enlace “Ver grabación” | color acento claro; en CSS custom podrías usar variable `--m3d-accent-soft` |

---

## Navegación (sticky)

| Elemento | Clases sugeridas |
|----------|------------------|
| Logo texto “MÁSTER 3D” | Tipografía sans bold; acento en “3D” con color `#0071e3` o clase `m3d-accent-word` en un `span` |
| Enlaces menú | En GHL: estilo de menú; si usas HTML custom: clases tipo `m3d-text-body` con `font-size` menor |
| Botón “AGENDAR CONSULTORÍA” | `m3d-btn m3d-btn-primary` |

---

## Hero (cabecera principal)

| Elemento | Clases (sin punto) |
|----------|-------------------|
| **Sección** contenedora | `m3d-section` (o padding manual) + `m3d-bg-white` |
| **Contenedor** ancho máximo | `m3d-container` |
| **Label** “Máster 3D Integral” (mono + gradiente) | `m3d-label-gradient` + opcional `m3d-fade-in` |
| **H1** título principal | `m3d-heading-hero` + `m3d-fade-in` + `m3d-fade-in-delay-1` |
| **Span** palabra “fuerza” (degradado azul) | `m3d-gradient-text` (envolver solo la palabra en un `span`) |
| **P** subtítulo grande (gris) | `m3d-text-body` (ajusta tamaño en GHL a `text-lg` equivalente si hace falta) + `m3d-fade-in` + `m3d-fade-in-delay-2` |
| **P** línea mono violeta (tagline) | `m3d-label` (sin gradiente) o estilo custom: mono + `color: var(--m3d-accent)` + `m3d-fade-in` + `m3d-fade-in-delay-2` |
| **Botón** CTA principal | `m3d-btn m3d-btn-primary` + `m3d-fade-in` + `m3d-fade-in-delay-3` |
| **Caja vídeo** / iframe | Contenedor con `m3d-rounded-2xl m3d-shadow-sm` + en el wrapper del vídeo: `m3d-float-anim` |

---

## Sección “Propuesta de valor / 3 Ejes” (slider)

| Elemento | Clases |
|----------|--------|
| Título de sección centrado | `m3d-heading-section m3d-text-center` |
| Label “Propuesta…” (azul fijo) | `m3d-label` (o color custom `#2F6FD6` en GHL) |
| Palabra “Beneficios” en acento | `span` con `m3d-accent-word` |
| **H3** tarjeta Eje (título multicolor) | `m3d-heading-card m3d-heading-gradient` |
| **P** cuerpo tarjeta | `m3d-text-small m3d-text-muted` |
| Flechas slider | Estilos GHL; si hay HTML: `border-radius` full + fondo glass (no incluido en CSS base; puedes añadir) |

---

## Sección “Para quién es” / tarjeta blanca

| Elemento | Clases |
|----------|--------|
| Label “¿Para Quién Es?” | `m3d-label-gradient` |
| **H2** | `m3d-heading-section` |
| Palabra “Este Máster” en rojo | `m3d-accent-red` en `span` |
| **H3** ítem lista | `m3d-heading-list` |
| **P** bajo cada h3 | `m3d-text-body` |

---

## Sección Programa / Organización

| Elemento | Clases |
|----------|--------|
| Label “PROGRAMA” | `m3d-label-gradient` |
| **H2** | `m3d-heading-section` |
| “Tu Transformación” en verde | `span` con `m3d-accent-green` |
| **P** intro | `m3d-text-body m3d-max-w-prose` |

---

## Testimonios

| Elemento | Clases |
|----------|--------|
| Label sección | `m3d-label` |
| **H2** | `m3d-heading-section` |
| **Blockquote** | `m3d-quote` |
| **P** nombre | `m3d-quote-source` |

---

## Profesorado (cards)

| Elemento | Clases |
|----------|--------|
| Label “Profesorado” | `m3d-label-gradient` (o `m3d-heading-section` tamaño reducido en GHL) |
| **H2** | `m3d-heading-section` |
| **P** intro | `m3d-text-body` |
| Tarjeta profesor | `m3d-card` |
| Cita (blockquote) | `m3d-quote` |

---

## Oferta / precios

| Elemento | Clases |
|----------|--------|
| **H2** / **H3** título bloque | `m3d-heading-card` o `m3d-heading-section` |
| **P** precio / letra pequeña | `m3d-text-small` |
| Botón reservar | `m3d-btn m3d-btn-primary` o `m3d-btn-dark` |

---

## Manifiesto

| Elemento | Clases |
|----------|--------|
| Label TechArtWorlds | `m3d-label-gradient` |
| **H2** | `m3d-heading-section` |
| Palabra en verde en título | `m3d-accent-green` |
| **P** párrafos | `m3d-text-body` |
| Imagen | `m3d-rounded-2xl m3d-shadow-sm` (contenedor) |

---

## FAQs / acordeón (contenido)

| Elemento | Clases |
|----------|--------|
| Título pregunta | `m3d-heading-list` |
| Respuesta | `m3d-text-body` |
| Lista con checks (popup) | `m3d-list-check` en `<ul>` |

---

## CTA flotante (fijo abajo)

En GHL suele ser un elemento “fixed”; estilos glass no están todos en el CSS base.  
Botón interno: `m3d-btn m3d-btn-dark` o `m3d-btn-primary` según diseño.

---

## Resumen rápido por etiqueta HTML

| Etiqueta | Clases típicas |
|----------|----------------|
| **h1** (hero) | `m3d-heading-hero` + animaciones opcionales |
| **h2** (sección) | `m3d-heading-section` |
| **h3** (card / lista) | `m3d-heading-card` o `m3d-heading-list` |
| **h3** (slider ejes, multicolor) | `m3d-heading-card m3d-heading-gradient` |
| **p** cuerpo | `m3d-text-body` |
| **p** secundario | `m3d-text-small` |
| **span** acento azul | `m3d-accent-word` |
| **span** acento rojo | `m3d-accent-red` |
| **span** acento verde | `m3d-accent-green` |
| **span** palabra degradada | `m3d-gradient-text` |
| **label** superior mono | `m3d-label` (sólido) o `m3d-label-gradient` |
| **a** botón violeta | `m3d-btn m3d-btn-primary` |
| **a** botón negro | `m3d-btn m3d-btn-dark` |
| **div** card | `m3d-card` |
| **div** shell + halo degradado | `m3d-block-shell` + hijo `m3d-gradient-glow` + contenido en `m3d-block-shell-front` |
| **section** collage fotos | `m3d-collage-section` — ver `snippets/ghl-photos-collage.html` |
| **blockquote** | `m3d-quote` |
| **ul** listado checks | `m3d-list-check` |

---

*Última actualización: alineado con `gohighlevel-custom.css` (animaciones, shell, photos collage, `m3d-gradient-glow`).*
