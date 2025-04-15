🧩 Módulos principales del backend
1. loader.py
    Carga campañas desde disco.
    Lee settings.json, entidades, textos e imágenes.
    Función: load_campaign(name: str) -> Campaign

2. campaign.py
Clase Campaign: maneja todo el ciclo de vida de una campaña.

Atributos: entities, currency, settings, texts, last_active, etc.

Métodos: update(), switch_to(), calculate_idle_gain(), reset_all()

3. entity.py
Clase Entity: representa un track individual.

value_current, value_total

level, level_thresholds, base_function, level_multiplier, reset_multiplier

update(tick: int) → evalúa función y actualiza valores.

check_level_up()

4. mathengine.py
Safe evaluator con fallback a y = x.

Usa sympy, eval, numexpr, o ast seguro.

Funciones:

compile_function(string: str) -> Callable

evaluate(f: Callable, x: float) -> float

test_function_output(f, range) -> list

5. scoring.py
Calcula puntuación por velocidad, precisión, letra correcta.

Controla barra de inclinación de campañas activas.

Control de bonus si se mantiene el extremo.

6. save_manager.py
Guarda automáticamente cada 5 minutos o al salir.

Carga desde /users/{user}/{campaign}/

Backup automático: zip de la carpeta del usuario.

Restauración desde ZIP.

7. user.py
Gestión de usuarios:

Lista usuarios disponibles.

Selección de usuario por defecto (config/app_settings.json)

Restaurar o exportar backups.

8. reset_engine.py
Controla el sistema de resets:

Cuenta resets totales por campaña.

Aplica reset_multiplier a producción.

9. ticker.py
Control del reloj del juego.

Corre tick() a intervalos definidos en settings.

Ignora campañas inactivas, solo calcula idle.

🔬 Tests
En /tests/:
validate_functions.py: carga funciones de entidades y las grafica.

simulate_output.py: genera una tabla con valores ejemplo de cada función.

test_entity_behavior.py: simula nivel, upgrade, reset y compara valores esperados.
