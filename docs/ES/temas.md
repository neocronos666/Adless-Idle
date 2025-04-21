# Sistema de Temas — Adless Idle

Esta guía describe cómo funciona el sistema de temas en **Adless Idle**, cómo crear nuevos temas y cómo personalizar la apariencia de la aplicación sin necesidad de editar el código.

---

## 🌐 Filosofía de diseño

- Todo tema debe poder ejecutarse con la menor cantidad de archivos posibles.
- Si faltan archivos, el motor intenta cargarlos desde el tema `default/`.
- Si el archivo tampoco existe en `default/`, se crea automáticamente con contenido básico.
- Un tema puede residir en la carpeta `themes/` o dentro de una campaña (`campaigns/<nombre>/theme/`).
- El usuario puede configurar si permite o no que una campaña cambie el tema activo.

---

## 🔍 Estructura básica de un tema

```
themes/
  ├── default/
      ├── theme.json
      ├── hud_config.json
      ├── palette.css
      ├── fonts/
      ├── backgrounds/
      ├── sounds/
      ├── animations/
      └── .files/ (SVGs)
```

> **Recomendado:** Copiar el tema `default/` como base y modificarlo.

---

## 📄 Archivos esenciales

### `theme.json`
Define configuraciones generales del tema:

```json
{
  "name": "default",
  "version": "1.0",
  "engine_version": ">=1.0.0",
  "mode": "dark",
  "fonts": {
    "main": "Poppins-Regular",
    "typewriter": "IMFellDWPicaSC-Regular",
    "hud": "Quicksand-Regular"
  },
  "sounds": {
    "notify": "notify.wav"
  },
  "background": {
    "dark": "bg_dark.jpg",
    "light": "bg_light.jpg"
  },
  "hud": {
    "hidden": ["progress_bar"]
  }
}
```

---

### `hud_config.json`
Opcional. Personaliza la disposición de los bloques del HUD:

```json
{
  "layout": {
    "menu_button": { "x": 0.05, "y": 0.95, "width": 0.1, "height": 0.08 },
    "entity_buttons": { "x": 0.5, "y": 0.85 }
  },
  "block_size": {
    "default": 0.15,
    "progress_bar": 0.05
  }
}
```

Si este archivo falta, se crea uno por defecto.

---

### `palette.css`
Archivo clave que contiene los colores del tema. Debe definir **al menos 5 colores base** y dos modos: `:root.dark` y `:root.light`

```css
:root.dark {
  --color-1: #00ff00;
  --color-2: #ff00ff;
  --color-3: #ffffff;
  --color-4: #000000;
  --color-5: #cccccc;
}

:root.light {
  --color-1: #228822;
  --color-2: #aa55dd;
  --color-3: #000000;
  --color-4: #ffffff;
  --color-5: #666666;
}
```

El motor selecciona el modo según `theme.json > mode`. Si un color falta, se reemplaza por `#000000`.

---

## 🌊 Fuentes personalizadas

El motor buscará fuentes en este orden:

1. Carpeta `fonts/` dentro del tema
2. Sistema operativo
3. Google Fonts (pendiente de implementación)

### Estructura esperada:
```
fonts/
  Poppins/
    Poppins-Regular.ttf
    Poppins-Bold.ttf
  Quicksand/
    Quicksand-Regular.ttf
  IM_Fell_DW_Pica_SC/
    IMFellDWPicaSC-Regular.ttf
```

El nombre usado en `theme.json` debe coincidir con el archivo `.ttf` sin la extensión.

---

## 🎧 Sonidos

Todos los sonidos deben estar en la carpeta `sounds/`. Su uso se define en `theme.json` (por ejemplo: `notify`, `click`, `error`, etc.).

El motor asegura que los sonidos no se superpongan.

---

## 💨 Animaciones y fondos

- Los fondos deben ir en `backgrounds/`.
- Las animaciones (ej. SVG animado o video corto) deben ir en `animations/`.
- Estos se seleccionan según el modo claro u oscuro en `theme.json`.

---

## 🔬 Nivel de personalización

| Nivel | Archivo | Descripción |
|-------|---------|-------------|
| ☄️ Básico | `palette.css` | Cambiar colores base |
| 🎨 Intermedio | `theme.json` | Cambiar fuentes, sonidos, fondos, HUD visible |
| 🔧 Avanzado | `hud_config.json` | Redefinir ubicaciones y tamaños de los bloques del HUD |

---

## ❓ Preguntas frecuentes

### ❌ Si falta un archivo, ¿falla el juego?
No. Si falta un archivo, se carga desde `default/`, y si tampoco existe, se crea automáticamente.

### 🚶‍♂️ ¿Puedo crear un tema que sólo cambia el color?
Sí. Solo necesitás un `palette.css`.

### 🎨 ¿Puedo crear un tema diferente por campaña?
Sí. Cada campaña puede incluir su propia carpeta `theme/`.

---

**Adless Idle** fue pensado para crecer desde la comunidad. Los temas son el primer paso para hacer tu experiencia totalmente propia ✨


