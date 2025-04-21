# Funciones matemáticas — Adless Idle

Este documento explica cómo se definen, evalúan y utilizan las funciones matemáticas en Adless Idle para determinar progresión, producción y escalado de dificultad.

---

## 🪜 ¿Qué es una función en Adless Idle?

Una función es una expresión matemática que representa:
- La progresión de una entidad (ej: nivel → producción)
- La cantidad ganada por segundo o por ciclo
- La curva de dificultad o desbloqueo

---

## ✏️ Sintaxis permitida

Las funciones deben ser cadenas de texto en formato Python seguro. Se permite el uso de:

### Operadores:
| Símbolo | Uso         | Ejemplo      |
|---------|-------------|--------------|
| `+`     | Suma        | `x + 5`      |
| `-`     | Resta       | `x - 3`      |
| `*`     | Multiplicación | `3 * x`  |
| `/`     | División    | `x / 2`      |
| `**`    | Potencia    | `x**2`       |

### Funciones seguras:
| Función       | Descripción             | Ejemplo              |
|---------------|-------------------------|-----------------------|
| `abs(x)`      | Valor absoluto          | `abs(x - 5)`          |
| `math.log(x)` | Logaritmo natural       | `math.log(x + 1)`     |
| `math.sin(x)` | Seno (para ciclos)      | `10 * math.sin(x/5)`  |
| `math.exp(x)` | Exponencial (crecimiento)| `math.exp(x/10)`     |

---

## ✅ Reglas generales

- La variable permitida es **x** (en minúsculas).
- No se puede usar ninguna otra variable ni llamada externa.
- No puede haber condicionales (`if`, `else`, `for`, etc.).
- Si la función no es válida, se reemplaza automáticamente por `x`.

---

## 🔢 Ejemplos de funciones comunes

| Propósito         | Función               | Comentario                       |
|------------------|------------------------|----------------------------------|
| Lineal simple     | `x`                    | Crecimiento constante            |
| Progresión leve   | `x**1.2 + 10`          | Crecimiento lento                |
| Difícil escalado  | `x**2 + 50`            | Mucho más difícil con cada nivel |
| Ganancia cíclica  | `10 * math.sin(x/4)`   | Para bonificaciones periódicas   |
| Logarítmica       | `math.log(x + 1)`      | Crece, pero se aplana rápido     |

---

## 🔧 Validación y fallback

El archivo `validate_function.py` asegura que las funciones:
- Sean válidas sintácticamente
- No contengan código peligroso
- Produzcan resultados numéricos

Si una función no pasa la validación, el motor la reemplaza por:
```python
y = x
```

---

## 📊 ¿Dónde se usan?

Las funciones se usan en:
- `gain_function`: ganancia por segundo o por ciclo
- `level_function`: escalado de producción por nivel
- `reset_multiplier`: bonus por cantidad de resets

Estas funciones se combinan en tiempo real, multiplicadas por:
- Nivel de entidad
- Eficacia del jugador
- Bonus temporales o de campaña

---

## ✨ Consejos para diseñadores

- Probar las funciones con `x` del 1 al 100 antes de usarlas.
- No usar valores negativos (se toman como cero).
- Para progresiones largas, usar logaritmos o raíces.
- Para recompensas, usar funciones con crecimiento exponencial.

---

**Adless Idle** permite usar funciones como lenguaje de diseño. Son el alma matemática de tu campaña ⚛️


