# Campañas — Adless Idle

Este documento explica cómo crear, editar y gestionar campañas en Adless Idle. Las campañas definen el contenido del juego: entidades, textos, imágenes, funciones y progresión.

---

## 📂 Estructura de carpeta

```
campaigns/
  ├── ads/                # Nombre de la campaña
  │   ├── config.json         # Configuración general de la campaña
  │   ├── texts/              # Textos traducibles por idioma
  │   ├── entities/           # Entidades con funciones matemáticas
  │   ├── images/             # Imágenes de cada entidad
  │   ├── videos/             # Animaciones o clips opcionales
  │   └── theme/              # (opcional) tema visual exclusivo de esta campaña
```

> Cada carpeta de campaña debe tener al menos un `config.json` para poder cargarse.

---

## 🔧 config.json

Define opciones generales:

```json
{
  "name": "Publicidad",
  "currency": "ad_points",
  "global_currency": false,
  "default_entity": "track001",
  "theme": true,
  "background": "fondo_ads.jpg"
}
```

- `theme`: si está en `true`, se buscará `/campaigns/ads/theme/` como tema temporal mientras dure la campaña.

---

## 📖 Textos traducibles

Los archivos deben estar nombrados por idioma (`EN_intro.json`, `ES_track001.json`, etc.)

### `texts/EN_intro.json`
```json
{
  "text": "Welcome to the world of advertising..."
}
```

### `texts/EN_track001.json`
```json
{
  "title": "Print Ads",
  "description": "Print ads were the first...",
  "typing_text": "Advertising is the soul of commerce."
}
```

---

## 📊 Entidades (`entities/`)

Cada archivo `trackXXX.json` representa una entidad (ej. TV, YouTube, radio, etc.)

### Estructura:
```json
{
  "level_function": "x**1.5 + 10",
  "gain_function": "5*x",
  "timer": 5,
  "show_progress": true,
  "typing_required": true,
  "level_requirements": [10, 20, 50, 100],
  "image": "track001.jpg"
}
```

#### Claves importantes:
- `level_function`: función que determina el poder de la entidad según su nivel.
- `gain_function`: determina cuánto genera por ciclo.
- `timer`: tiempo entre ciclos en segundos.
- `show_progress`: muestra u oculta la barra de progreso.
- `typing_required`: habilita el bloque de tipeo activo.
- `level_requirements`: puntos requeridos acumulados para subir de nivel.
- `image`: archivo de imagen que representa la entidad.

---

## 🌄 Recompensas y desbloqueos

- Las entidades deben aparecer de forma progresiva.
- Al cumplir las condiciones de una entidad, se desbloquea la siguiente.
- Es posible diseñar campañas donde algunas entidades solo aparezcan si otras campañas están activas.

---

## 📈 Progresión y resets

- Las funciones son matemáticas y personalizables.
- Los resets permiten cambiar de función base a otra más empinada.
- El progreso se acumula y se guarda por usuario, por campaña.

---

## 🔄 Compatibilidad con temas

Una campaña puede tener su propia carpeta `theme/`:
```
campaigns/ads/theme/
  ├── theme.json
  ├── hud_config.json
  ├── palette.css
```

- Se cargará temporalmente al iniciar la campaña si `theme: true` en `config.json`.
- El usuario puede decidir si permitirlo o no en `settings.json` global.

---

## 🎨 Imagen e identidad

- Las imágenes están en `images/` con nombres como `track001.jpg`.
- Los textos pueden tener tono humorístico, educativo, sarcástico, etc.
- Cada campaña es una narrativa con ritmo, personajes y estética.

---

## ⚡ Plantillas

Existe una plantilla en:
```
campaigns/template/
```
Que incluye:
- `config.json`
- Un archivo de entidad ejemplo
- Archivos de texto y ayuda (`help.md`)

---

**Adless Idle** permite crear juegos educativos, temáticos, cómicos o experimentales. Las campañas son la forma de contar historias mientras se juega ✨


