# Estructura del motor (engine) — Adless Idle

Este documento explica cómo está organizado el motor interno del juego: sus componentes, responsabilidades y ubicación de archivos.

---

## 📂 Estructura del directorio `/engine`

```
/engine/
├── utils/            # Herramientas y funciones auxiliares
├── views/            # Vistas gráficas (HUD, pantallas)
├── ui/               # Interfaz y componentes reutilizables (futuro)
```

---

## ⚙️ `/engine/utils/`
Contiene código reutilizable y lógico, no visual:

### Archivos:

| Archivo                    | Descripción                                                |
|----------------------------|------------------------------------------------------------|
| `color.py`                 | Utilidades para manipular colores (RGB, conversión)        |
| `css_parser.py`            | Lector de archivos `palette.css`                           |
| `default_theme.py`         | Contiene los archivos por defecto para un tema base        |
| `logger.py`                | Configura y registra los logs de debug                     |

### Funcionalidades futuras:
- Validador de rutas
- Gestor de sonido
- Gestor de traducciones

---

## 📊 `/engine/views/`

Contiene clases que dibujan en pantalla:

### Archivos:

| Archivo            | Descripción                                            |
|--------------------|--------------------------------------------------------|
| `hud.py`           | Clase `HUDLayout`, responsable del HUD visual         |
| `campaign_view.py` | Vista de campaña y renderizado de entidades (WIP)     |

---

## 🔹 Integración con el resto del proyecto

- El motor no debe contener datos de campañas.
- Los datos del usuario, temas y campañas se cargan por separado.
- Las vistas reciben datos ya cargados y los renderizan.
- Los temas definen los estilos, pero no modifican el motor directamente.

---

## ✨ Filosofía del engine

- Modular y desacoplado
- Componentes reutilizables
- Separación entre lógica, vista y datos
- Facilita testeo, mantenimiento y extensión

---

**Adless Idle** busca ser un framework ligero para juegos idle visuales, donde el engine actúa como intermediario entre los datos cargados y la experiencia del jugador ⚛️


