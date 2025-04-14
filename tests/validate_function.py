# tests/validate_functions.py

import matplotlib.pyplot as plt
import numpy as np
import json
import os
import ast
import math

# Fallback function
def fallback(x):
    return x

# Safe evaluation using AST (no eval directa)
def safe_compile(expr: str):
    try:
        node = ast.parse(expr, mode='eval')
        allowed_nodes = (
            ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant, ast.Name,
            ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod,
            ast.Load, ast.Call
        )
        for subnode in ast.walk(node):
            if not isinstance(subnode, allowed_nodes):
                raise ValueError(f"Unsafe node: {type(subnode).__name__}")
            if isinstance(subnode, ast.Call) and not isinstance(subnode.func, ast.Name):
                raise ValueError("Unsafe function call structure")
        def f(x):
            allowed_names = {"x": x, "math": math, **vars(math)}
            return eval(compile(node, "<string>", "eval"), {"__builtins__": {}}, allowed_names)
        return f
    except Exception as e:
        print(f"[ERROR] Function fallback to y=x → {e}")
        return fallback

# Cargar funciones desde archivo
def load_functions(path: str):
    with open(path, "r") as f:
        data = json.load(f)
    return data

# Graficar una función
def graph_function(name: str, f, xmin=0, xmax=100, steps=200):
    x = np.linspace(xmin, xmax, steps)
    try:
        y = [f(val) for val in x]
        plt.plot(x, y, label=name)
    except Exception as e:
        print(f"[ERROR] Falló la función {name}: {e}")

# Ejecutar test desde una lista
def run_tests(json_path: str):
    functions = load_functions(json_path)
    for name, func_expr in functions.items():
        print(f"\n{name}: {func_expr}")
        f = safe_compile(func_expr)
        try:
            values = [f(x) for x in range(0, 21)]
            for i, val in enumerate(values):
                print(f"x={i} → y={val}")
            graph_function(name, f)
        except Exception as e:
            print(f"[ERROR] Fallo en evaluación de {name}: {e}")
    plt.title("Funciones de Entidad")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_tests("test_functions.json")

