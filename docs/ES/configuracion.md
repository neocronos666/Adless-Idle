# Configuración — Adless Idle

Este documento describe los archivos de configuración general del juego, los temas y los usuarios.

---

## 🔧 settings.json

Ubicación: raíz del proyecto
```bash
/settings.json
```

Este archivo define la configuración global de la app:

```json
{
  "language": "es",
  "user": "default",
  "theme": "default",
  "allow_campaign_theme": true,
  "prompt_before_theme_change": true,
  "debug": true
}
```

### Claves:
- `language`: Idioma por defecto (`es`, `en`, etc.)
- `user`: Usuario actual cargado
- `theme`: Tema visual actual (carpeta en `/themes/` o dentro de campaña)
- `allow_campaign_theme`: Permite que una campaña use su propio tema temporal
- `prompt_before_theme_change`: Pregunta antes de cambiar de tema por campaña
- `debug`: Si es `true`, activa el sistema de logs en `/logs/`

---

## 👤 user/<nombre>/user.json

Ubicación: carpeta de cada usuario

```bash
/user/<usuario>/user.json
```

Ejemplo:
```json
{
  "name": "neocronos",
  "language": "es",
  "theme": "default",
  "fullscreen": false,
  "audio": true,
  "last_campaign": "ads"
}
```

- Cada usuario tiene su propia configuración
- Se pueden guardar progresos independientes
- Se pueden guardar campañas activas distintas

---

## ✅ Valores por defecto

Si alguno de estos archivos no existe:
- El sistema lo genera automáticamente con valores básicos
- El tema `default` se usa como base para todo

---

## 📂 Otros archivos relacionados

### `theme.json` (dentro de cada tema):
Define propiedades visuales del tema, colores y fuentes.

### `hud_config.json`:
Define posiciones, tamaños y visibilidad de bloques del HUD.

---

## 🔢 Modo debug y logs

Si `debug: true`, todos los eventos importantes se registran en:
```
/logs/YYMMDD_TIPO.log
```

Cada script importante (loader, theme_loader, logger) escribe su log.

---

**Adless Idle** tiene un enfoque modular: cada parte del juego se puede configurar, personalizar o extender sin editar código fuente ✨


