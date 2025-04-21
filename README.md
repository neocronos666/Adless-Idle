# Adless Idle

**Versión actual:** 0.0.5 pre-ALPHA  
**Repositorio:** [Neocronos666/Adless-Idle](https://github.com/Neocronos666/Adless-Idle)  
**Licencia:** MIT  

---

## 🌟 Filosofía del proyecto

**Adless Idle** es un motor de juegos idle libre, educativo y completamente personalizable, diseñado para correr con la mínima cantidad de archivos posibles. No incluye publicidad ni dependencias invasivas. El objetivo es brindar a usuarios y desarrolladores una base robusta, limpia y accesible para crear juegos tipo *idle* con funciones matemáticas personalizadas, texto educativo y elementos visuales intercambiables.

> Todo es un archivo: desde la configuración hasta el diseño de la interfaz. El motor está pensado para que absolutamente todo pueda ser modificado, extendido o versionado sin tocar el código base.

- Sin anuncios.  
- Sin rastreadores.  
- Completamente personalizable.  
- Multiplataforma.  
- Pensado para mods y campañas creadas por la comunidad.

---

## 🚀 Instalacion de desarrollo desde el repositorio
A continuacion los pasos para clonar el repositorio y correr la version en desarrollo.
Para jugar se aconseja instalar desde el paquete de instalacion de cada plataforma (A DETERMINAR)

### 1. Clonar el repositorio
```bash
git clone https://github.com/Neocronos666/Adless-Idle.git
cd Adless-Idle
```

### 2. Crear entorno e instalar dependencias
```bash
#Dar permisos de ejecución a los scripts
chmod +x bash-scripts/create-env.sh
chmod +x bash-scripts/setup-arcade.sh

#Crear el entorno
sudo bash bash-scripts/create-env.sh

#Activar el entorno
source adless_ilde_env/bin/activate

#Instalar las dependencias
sudo bash bash-scripts/setup-arcade.sh
```

### 3. Ejecutar el juego
```bash
python main.py
```

---

## 📁 Contenido principal

| Carpeta | Descripción |
|--------|-------------|
| `campaigns/` | Campañas del juego (ADS, templates, etc). Cada una puede tener su propio tema. |
| `themes/` | Temas visuales reutilizables para el HUD y estilo. Incluye fuentes, paletas, sonidos. |
| `engine/` | Módulo principal del motor: vistas, lógica, utilidades, logger, parser CSS, etc. |
| `tests/` | Tests automáticos con Pytest para componentes del backend y visuales. |
| `user/` | Datos de usuarios. Cada subcarpeta representa un perfil, con configuración y progresos. |

> Ver [docs/estructura.md](docs/estructura.md) para una descripción completa de carpetas y archivos.

---

## 🎭 Características principales

- ✅ Sistema de temas con fallback inteligente (si falta un archivo, se crea o se carga el default).
- ✅ Soporte para funciones matemáticas personalizadas: progresión lineal, cuadrática, logarítmica, etc.
- ✅ Tipado de texto educativo con sistema de puntuación (velocidad vs precisión).
- ✅ Barra de progreso que responde a la acción del jugador (modo activo vs modo idle).
- ✅ Campañas modulares con divisas propias y condicionales desbloqueables.
- ✅ Todos los textos traducibles por archivo y por idioma (`EN_`, `ES_`, etc).
- ✅ Registro y carga de usuarios con guardado individual por campaña.

---

## 🚪 Modo de edición y personalización

- Los temas pueden vivir en `themes/` o dentro de una campaña (`campaigns/ads/theme/`), según el estilo buscado.
- Si se permite, una campaña puede cambiar el tema activo. Esto se controla desde `settings.json`.
- La filosofía de diseño permite tres niveles de modding:
  - ✨ Cambiar colores desde `palette.css`
  - ✏️ Modificar la interfaz en `theme.json`
  - 🔧 Rediseñar el HUD desde `hud_config.json`

---

## 📖 Documentación adicional

- [docs/ES/estructura.md](docs/ES/estructura.md) — estructura de carpetas
- [docs/ES/temas.md](docs/ES/temas.md) — crear y editar temas
- [docs/ES/campanas.md](docs/ES/campanas.md) — estructura de campañas
- [docs/ES/usuarios.md](docs/ES/usuarios.md) — gestion de usuarios
- [docs/ES/funciones.md](docs/ES/funciones.md) — uso de las funciones matematicas
- [docs/ES/hud.md](docs/ES/hud.md) — diseño y filosofia de la app
- [docs/ES/configuracion.md](docs/ES/configuracion.md) — configuracion del juego
- [docs/ES/motor.md](docs/ES/motor.md) — documentacion del motor del juego (en progrreso)

---

## 🤝 Colaborar

El proyecto está en versión **pre-alpha**, pero ya podés:

roadmap

- Reportar bugs o sugerencias en [Issues](https://github.com/Neocronos666/Adless-Idle/issues)
- Enviar pull requests para mejorar temas, campañas, testeo o documentación

> No es necesario saber mucho de Python para colaborar. Si sabés diseñar, escribir o traducir, también podés sumarte.

---

Desarrollado con pasión por **Neocronos666**  
Adless Idle: *Tu juego idle, sin Ads.*


