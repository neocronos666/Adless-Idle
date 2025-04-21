# Estructura de Carpetas — Adless Idle

Este documento describe la estructura de archivos y carpetas del proyecto **Adless Idle**, detallando el contenido de cada una, su propósito y qué se espera encontrar dentro.

---

## 🗂️ Raíz del Proyecto

| Carpeta / Archivo | Descripción |
|-------------------|-------------|
| `main.py` | Punto de entrada del juego. Carga configuraciones y lanza la interfaz. |
| `settings.json` | Configuración general de la aplicación (idioma, tema activo, modo debug, etc.). |
| `theme_loader.py` | Módulo encargado de cargar temas desde archivos. |
| `loader.py` | Módulo de carga general (config, usuarios, campañas). |
| `validate_function.py` | Utilidad para validar funciones matemáticas usadas en entidades. |
| `README.md` | Descripción general del proyecto. |
| `docs/` | Documentación extendida del proyecto en Markdown. |
| `todo.md` | Tareas pendientes del desarrollador. |
| `logger.py` | Logger general si no se usa desde `engine/utils`. |


---

## 🪪 `adless_idle_env/`
Contiene el entorno virtual Python del proyecto. No debe modificarse ni subirse al repositorio.

> Recomendado ignorar con `.gitignore`

---

## 📤 `bash-scripts/`
Scripts para automatizar instalación y entorno:

| Archivo | Descripción |
|---------|-------------|
| `create-env.sh` | Crea el entorno virtual y lo activa. |
| `setup-arcade.sh` | Instala dependencias necesarias (Arcade, pyglet, etc.). |

---

## 🏙️ `themes/`
Temas visuales. Cada subcarpeta es un tema completo.

### `themes/default/`
| Archivo/Carpeta | Descripción |
|------------------|-------------|
| `theme.json` | Define fuentes, modo, sonidos, fondo, versión compatible. |
| `hud_config.json` | Configuración del HUD. Bloques, tamaños, visibilidad. |
| `palette.css` | Paleta de colores del tema. Debe incluir 5 colores base y modo claro/oscuro. |
| `fonts/` | Fuentes personalizadas locales. |
| `sounds/` | Efectos de sonido del tema. |
| `animations/` | Animaciones opcionales (ej. SVG, videos). |
| `backgrounds/` | Imagen de fondo del HUD. |
| `.files/` | Archivos SVG para la distribución de bloques. |

---

## 🌐 `campaigns/`
Contiene todas las campañas del juego. Cada carpeta representa una.

### Estructura de una campaña
| Carpeta/Archivo | Descripción |
|------------------|-------------|
| `config.json` | Configuración principal de la campaña (divisa, nombre, fondo, etc.). |
| `entities/` | Entidades del juego (`track000.json`, `track001.json`, etc.). |
| `texts/` | Archivos de texto por idioma (`EN_intro.json`, `ES_track001.json`). |
| `images/` | Imagenes de las entidades o ilustraciones. |
| `videos/` | Clips o animaciones opcionales. |
| `theme/` | (opcional) Tema exclusivo de la campaña. Tiene misma estructura que `themes/`. |
| `help.md` | Documentación específica de la campaña (opcional). |

### Ejemplo de campañas:
- `campaigns/template/`: plantilla para crear nuevas campañas.
- `campaigns/ads/`: campaña educativa sobre la historia de la publicidad.

---

## 💡 `engine/`
El motor principal del juego.

| Subcarpeta | Descripción |
|------------|-------------|
| `views/` | Interfaz y vistas principales (`hud.py`, `campaign_view.py`). |
| `ui/` | Elementos de interfaz gráfica reutilizables (por implementar). |
| `utils/` | Utilidades del motor: logger, parser CSS, tema por defecto. |

---

## 🔧 `tests/`
Tests automáticos con Pytest. Incluye validación de funciones, logger, loader de tema, HUD, etc.

| Archivo | Prueba |
|---------|--------|
| `test_theme_loader.py` | Carga de temas y fallback por defecto. |
| `test_validate_function.py` | Validación de funciones matemáticas. |
| `test_logger.py` | Registro y escritura de logs. |
| `test_hud_layout.py` | Render del HUD desde datos de tema. |
| `test_functions.json` | Datos de funciones para testear. |

> Se ejecutan con `pytest` desde la raíz del proyecto.

---

## 👤 `user/`
Gestión de perfiles de jugador. Cada subcarpeta es un nombre de usuario.

### Estructura:
```
/user/
  └── nombre_usuario/
        ├── user.json         # Configuraciones generales del jugador
        ├── ads.json          # Progreso de la campaña "ads"
        └── otra.json         # Progreso de otras campañas
```

> El usuario por defecto es `default`. Si no existe, se crea automáticamente.

---

## 💤 `logs/`
Contiene los registros de la aplicación, por fecha y módulo.

| Ejemplo de nombre | Descripción |
|-------------------|-------------|
| `250419_THEME.log` | Logs del loader de temas en modo debug. |
| `250419_LOADER.log` | Logs del loader general. |

> Solo se generan si `debug = true` en `settings.json`.

---

## ⚫ Directorios ignorados

Estos directorios se excluyen del repositorio mediante `.gitignore`:

- `__pycache__/`
- `.pytest_cache/`
- `.deprecated/`
- `.git/`
- `logs/`
- `adless_idle_env/`

---

Esta estructura puede ampliarse en futuras versiones para incluir:

- `mods/`: extensiones de usuarios
- `locales/`: archivos de traducción por idioma
- `builder/`: empaquetado por plataforma (Windows/Linux/Android)

---

✨ *Adless Idle está pensado para crecer, modularizarse y adaptarse a tus ideas.*


