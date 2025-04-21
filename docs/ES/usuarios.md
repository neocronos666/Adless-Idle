# Sistema de Usuarios y Funciones — Adless Idle

Este documento explica cómo funciona el sistema de usuarios y cómo se definen y validan las funciones matemáticas dentro del juego.

---

## 👤 Sistema de Usuarios

Cada usuario tiene una carpeta propia dentro de:
```
/user/<nombre_usuario>/
```

### Archivos:
```
/user/default/user.json           # Configuración general del usuario
/user/default/ads.json            # Progreso en la campaña 'ads'
/user/default/<campaña>.json      # Progreso para otras campañas
```

### user.json
Contiene las preferencias individuales del usuario:
```json
{
  "name": "default",
  "language": "es",
  "theme": "default",
  "last_campaign": "ads",
  "fullscreen": true,
  "audio": true
}
```

- El archivo se genera automáticamente si no existe.
- El usuario por defecto es `default`, a menos que se especifique en `settings.json`.
- Cada campaña guarda su progreso por separado en un archivo con el nombre de la campaña.



---

**Adless Idle** usa funciones como mecánica central, permitiendo progresiones totalmente personalizables, educativas y experimentales ✨


