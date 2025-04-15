# tests/validate_functions.py

import matplotlib.pyplot as plt
import numpy as np
import json
import os
import ast
import math

allowed_nodes = (
    ast.Expression, ast.BinOp, ast.UnaryOp,
    ast.Constant, ast.Name, ast.Call, ast.Load,
    ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod,
    ast.UAdd, ast.USub, ast.Attribute
)

allowed_math_funcs = {"log", "sin", "cos", "tan", "sqrt", "exp", "log10"}
allowed_names = {"x", "math"}

def is_safe_ast(node):
    for subnode in ast.walk(node):
        if not isinstance(subnode, allowed_nodes):
            return False
        if isinstance(subnode, ast.Name):
            if subnode.id not in allowed_names:
                return False
        if isinstance(subnode, ast.Call):
            # Asegurar que sea math.func, y que func esté en lista blanca
            if not isinstance(subnode.func, ast.Attribute):
                return False
            if not isinstance(subnode.func.value, ast.Name):
                return False
            if subnode.func.value.id != "math":
                return False
            if subnode.func.attr not in allowed_math_funcs:
                return False
    return True

def validate_function(expr: str):
    try:
        tree = ast.parse(expr, mode="eval")
        if not is_safe_ast(tree):
            raise ValueError("Unsafe function call structure")
        return eval(f"lambda x: {expr}", {"math": math})
    except Exception as e:
        print(f"[ERROR] Function fallback to y=x → {e}")
        return lambda x: x  # fallback seguro

# Fallback function
def fallback(x):
    return x

# Safe evaluation using AST (no eval directa)
def safe_compile(expr: str):
    try:
        node = ast.parse(expr, mode='eval')
        allowed_nodes = (
            ast.Expression, ast.BinOp, ast.UnaryOp,
            ast.Constant, ast.Name, ast.Call, ast.Load,
            ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod,
            ast.UAdd, ast.USub, ast.Attribute
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
    run_tests("/tests/test_functions.json")

