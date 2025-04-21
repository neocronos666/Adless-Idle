# HUD (Head-Up Display) — Adless Idle

Este documento describe la estructura, componentes y comportamiento del HUD (Head-Up Display) del juego Adless Idle.

---

## 🎨 Filosofía visual

El HUD es el corazón visible del juego. Debe ser informativo, modular y agradable visualmente, sin sobrecargar al jugador.

- Estilo retro-minimalista inspirado en juegos de DOS.
- Paleta tomada del tema activo (por defecto: `default/palette.css`).
- Adaptativo: se ajusta a dispositivos móviles o escritorio.

---

## 🔹 Componentes básicos del HUD

Cada tema puede reordenar o esconder bloques. El HUD por defecto contiene:

| Bloque                | Descripción                                              |
|-----------------------|----------------------------------------------------------|
| Menú                  | Esquina superior izquierda, ícono ≡                      |
| Entidades activas     | Lista vertical de entidades desbloqueadas (botones)      |
| Barra de progreso     | Muestra avance por precisión o velocidad                 |
| Panel de mejoras      | Muestra info, stats y mejoras de la entidad activa       |
| Zona de tipeo         | Texto a tipear, letras resaltadas, detección de errores  |
| Temporizador          | Progreso visual y cálculo por segundos                   |
| Indicadores globales  | Puntos, divisas, multiplicadores, estadísticas           |
| Fondo animado         | Imagen estática con efecto visual (opcional)             |

---

## ⚖️ Configuración desde hud_config.json

Cada tema incluye `/theme/hud_config.json` donde se define:

```json
{
  "layout": {
    "menu": [0.05, 0.95, 0.1, 0.08],
    "typing_area": [0.5, 0.15, 0.9, 0.1],
    "progress_bar": [0.5, 0.25, 0.8, 0.02],
    ...
  },
  "block_size": {
    "entity_button": [0.9, 0.1],
    "upgrade_card": [0.8, 0.2]
  }
}
```

Los valores están en proporción al tamaño de la ventana: `[x, y, width, height]`

---

## 🌿 Personalización

Cada tema puede modificar:

- Posición y tamaño de los bloques
- Colores y tipografía (via `palette.css` y `theme.json`)
- Mostrar u ocultar bloques (vía `theme.json > hud.hidden[]`)
- Animaciones suaves entre cambios de vista o desbloqueos

---

## 🚀 Tipeo como mecánica activa

- El texto a tipear se define por entidad (`typing_text` en archivo de texto).
- El jugador puede ganar más puntos si teclea correctamente.
- Se premia:
  - Tecla correcta (doble puntos)
  - Espacio correcto (triple puntos)
- Si se equivoca, se pierde progreso visual momentáneamente.

---

## 🔢 Progreso visual

- Una barra se desplaza hacia la derecha (precisión) o izquierda (velocidad).
- Al llegar a extremos otorga multiplicadores temporales.
- Se resetea si se detiene el tipeo o si hay muchos errores.

---

## 📆 Animaciones y estilo

- El fondo puede tener un efecto visual sutil (parallax, desplazamiento, brillos).
- Los botones y barras pueden tener pequeñas transiciones.
- Las fuentes del HUD se definen en `theme.json > fonts`.

---

## 🌐 Adaptabilidad

- En pantallas móviles verticales: bloques apilados.
- En escritorio: se puede reordenar horizontalmente.
- Futuro: posibilidad de elegir HUD por campaña.

---

El HUD es más que una interfaz: es la conexión entre jugador, campaña y progreso. Cada diseño puede contar una historia visual distinta ✨


