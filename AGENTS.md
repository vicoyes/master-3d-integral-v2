# Sistema de Diseño — MASTER 3D INTEGRAL
## "Mismos colores. Otra dimensión."

> El objetivo no es rediseñar la web — es inyectarle **alma**. Los colores, fuentes y estructura permanecen. Lo que cambia es la *presencia*, la *intención* y el *ritmo* visual.

---

## 🔍 Diagnóstico: Lo que falta hoy

| Dimensión | Estado actual | Lo que debería ser |
|-----------|--------------|-------------------|
| **Primer glow** | No existe — el hero es plano | Un foco de luz que llama la atención antes de leer |
| **Tipografía hero** | Tamaño correcto pero genérico | Editorial, con jerarquía dramática |
| **Copy como diseño** | Informativo pero frío | Cada frase tiene peso, pausa, intención |
| **Los Ejes (X/Y/Z)** | Se mencionan, no se *sienten* | Son el sistema visual de toda la página |
| **Ritmo de scroll** | Sección tras sección, plano | Cinematográfico — cada sección es un acto |
| **Texturas** | Fondo negro puro | Negro con profundidad (noise, vignette sutil) |
| **Micro-detalles** | Ninguno | Separadores, badges, líneas vivas |

---

## 🎯 El Concepto: "Las 3 Dimensiones"

- **Eje X → Color naranja/ámbar** (#E8733A) — Formación 3D
- **Eje Y → Color violeta** (#7C6FE8) — Orden Interno
- **Eje Z → Color verde/teal** (#3A9E82) — Negocio

Cada vez que aparece un eje, su color lo precede. El usuario no necesita leer la etiqueta — ya *siente* de qué eje se trata.

---

## 🎨 Sistema de Color

```css
:root {
 /* Base */
 --bg-primary: #0A0A0F; /* negro con tinte azul */
 --bg-surface: #111118; /* superficies */
 --accent-orange: #E8733A; /* naranja principal — Eje X */
 --text-primary: #F2F2F0; /* blanco suave */
 --text-muted: rgba(242,242,240,0.45);

 /* Ejes como sistema de color */
 --eje-x: #E8733A; /* naranja — Formación 3D */
 --eje-x-glow: rgba(232,115,58,0.15);
 --eje-y: #7C6FE8; /* violeta — Orden Interno */
 --eje-y-glow: rgba(124,111,232,0.15);
 --eje-z: #3A9E82; /* verde — Negocio */
 --eje-z-glow: rgba(58,158,130,0.15);

 /* Profundidad */
 --noise-opacity: 0.035;
}
```

---

## ✍️ Tipografía

```css
/* Hero headline — en 3 líneas distintas con tamaños distintos */
.hero-line-1 {
 font-size: clamp(14px, 1.5vw, 18px);
 letter-spacing: 0.15em;
 text-transform: uppercase;
 color: var(--eje-x);
 font-weight: 400;
}
.hero-line-2 {
 font-size: clamp(48px, 7vw, 96px);
 font-weight: 600;
 line-height: 1.0;
 letter-spacing: -0.03em;
}
.hero-line-3 {
 font-size: clamp(32px, 4.5vw, 56px);
 font-weight: 300;
 color: var(--text-muted);
 line-height: 1.15;
}

/* Labels de eje */
.eje-label {
 font-size: 11px;
 font-weight: 600;
 letter-spacing: 0.18em;
 text-transform: uppercase;
}

/* Números monumentales */
.stat-number {
 font-size: clamp(56px, 8vw, 96px);
 font-weight: 700;
 line-height: 0.9;
 letter-spacing: -0.04em;
}
```

---

## 🌫️ Hero Glow — Sistema de 3 focos

```css
.hero-atmosphere {
 position: absolute;
 inset: 0;
 pointer-events: none;
 overflow: hidden;
}

/* Foco principal — naranja, Eje X, centrado arriba */
.hero-atmosphere::before {
 content: '';
 position: absolute;
 top: -15%;
 left: 50%;
 transform: translateX(-50%);
 width: 700px;
 height: 500px;
 background: radial-gradient(ellipse,
 rgba(232,115,58, 0.18) 0%,
 rgba(232,115,58, 0.05) 50%,
 transparent 70%
 );
 filter: blur(60px);
}

/* Foco secundario — violeta, Eje Y */
.hero-atmosphere::after {
 content: '';
 position: absolute;
 top: 10%;
 left: 30%;
 width: 400px;
 height: 300px;
 background: radial-gradient(ellipse,
 rgba(124,111,232, 0.1) 0%,
 transparent 70%
 );
 filter: blur(80px);
}
```

---

## 🧩 Componentes

### Badges de Eje
```css
.eje-badge {
 display: inline-flex;
 align-items: center;
 gap: 8px;
 padding: 6px 14px 6px 10px;
 border-radius: 9999px;
 border: 1px solid currentColor;
 font-size: 11px;
 font-weight: 600;
 letter-spacing: 0.15em;
 text-transform: uppercase;
}
.eje-badge--x { color: var(--eje-x); border-color: rgba(232,115,58, 0.35); background: rgba(232,115,58, 0.08); }
.eje-badge--y { color: var(--eje-y); border-color: rgba(124,111,232, 0.35); background: rgba(124,111,232, 0.08); }
.eje-badge--z { color: var(--eje-z); border-color: rgba(58,158,130, 0.35); background: rgba(58,158,130, 0.08); }
.eje-badge::before { content: ''; width: 6px; height: 6px; border-radius: 50%; background: currentColor; flex-shrink: 0; }
```

### Cards con acento de eje
```css
.card-eje-x {
 border: 1px solid rgba(232,115,58, 0.15);
 border-top: 2px solid var(--eje-x);
 background: rgba(232,115,58, 0.03);
}
```

### CTA Principal
```css
.btn-cta {
 background: var(--eje-x);
 color: #fff;
 border: none;
 border-radius: 9999px;
 padding: 16px 32px;
 font-size: 15px;
 font-weight: 600;
 position: relative;
 overflow: hidden;
}
.btn-cta::after {
 content: '';
 position: absolute;
 inset: 0;
 background: linear-gradient(135deg, rgba(255,255,255,0.15) 0%, transparent 60%);
}
.btn-cta:hover {
 transform: translateY(-1px);
 box-shadow: 0 8px 32px rgba(232,115,58, 0.35);
}
```

### Separadores con glow
```css
.section-divider {
 width: 100%;
 height: 1px;
 background: linear-gradient(90deg, transparent 0%, rgba(232,115,58, 0.4) 50%, transparent 100%);
 margin: 80px 0;
}
```

### Stats Grid Monumental
```css
.stats-grid {
 display: grid;
 grid-template-columns: repeat(3, 1fr);
 gap: 1px;
 background: rgba(255,255,255,0.08);
 border-radius: 16px;
 overflow: hidden;
}
.stat-cell { background: var(--bg-surface); padding: 48px 32px; text-align: center; }
.stat-number { font-size: 72px; font-weight: 700; line-height: 0.9; letter-spacing: -0.04em; }
.stat-unit { font-size: 13px; color: var(--text-muted); letter-spacing: 0.12em; text-transform: uppercase; margin-top: 12px; }
```

---

## 🎬 Ritmo de Scroll — Estructura de Actos

```
ACT I — EL PROBLEMA
 Hero: El glow. La promesa. El CTA.

ACT II — LOS 3 EJES
 Aparición progresiva: Eje X → Eje Y → Eje Z con sus colores.

ACT III — LA PRUEBA
 Testimonios como citas de revista.

ACT IV — EL SISTEMA
 Horario semanal tratado como infografía.

ACT V — LOS HUMANOS
 Equipo con sus frases primero.

ACT VI — LA DECISIÓN
 Pricing + CTA final con número grande.
```

---

## 📜 Copy Clave

### Hero Subheadline
> "Para hacer de ti un profesional próspero. Y una persona que duerme tranquila."

### Barra de anuncio
> "⚡ 3 plazas disponibles para la próxima edición — Agendar consultoría →"

---

## 🧭 Prioridad de Implementación

**Impacto alto / Esfuerzo bajo:**
1. ✅ Añadir hero glow (CSS puro, 20 líneas)
2. ✅ Convertir "Eje X/Y/Z" en badges de color
3. ✅ Añadir letter-spacing y font-weight: 300 al subtítulo del hero
4. ✅ Cambiar copy del precio — frase comparativa
5. ✅ Añadir separadores con glow entre secciones

**Impacto alto / Esfuerzo medio:**
6. 🔶 Rediseñar stats como grid monumental
7. 🔶 Animar entradas con scroll (IntersectionObserver)
8. 🔶 Revisar copy de "¿Para quién es?"
9. 🔶 Añadir textura de noise al fondo

**Impacto medio / Esfuerzo alto:**
10. 🔵 Infografía del horario semanal
11. 🔵 Testimonios como citas editoriales

---

## 🚫 Lo que NO cambiar

- ❌ Los colores base — naranja, negro profundo, blanco suave funcionan
- ❌ La estructura de secciones — el orden narrativo ya es correcto
- ❌ La tipografía base — solo ajustar escalas y pesos
- ❌ El copy de los ejes — el concepto X/Y/Z es diferenciador
- ❌ El manifiesto final — es el alma de la marca

---

## 💡 La Frase que Resume Todo

> "No es el mejor diseño el que gana. Es el que hace que el visitante sienta que ya confía en ti antes de terminar de leer el hero."

---

*Documento de diseño — Master 3D Integral — Abril 2026*
