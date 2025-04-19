# tests/test_theme_loader.py
import os
import sys
import pytest


# Agrega el directorio raíz al sys.path
#sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from theme_loader import ThemeLoader

def test_theme_loader_basic():
    # Carga el tema por defecto
    loader = ThemeLoader(theme_name="default", debug=True)
    data = loader.get_theme_data()

    print("\n--- THEME DATA ---")
    for key, val in data.items():
        print(f"{key}: {val if not isinstance(val, dict) else '[dict]' }")

    assert data is not None
    assert data["name"] == "Default"
    assert "palette" in data
    assert isinstance(data["palette"], dict)
    assert "fonts" in data
    assert "paths" in data["fonts"]
    assert "hud" in data
    assert "layout" in data["hud"]


def test_theme_palette_colors():
    loader = ThemeLoader(theme_name="default")
    palette = loader.get_theme_data()["palette"]

    print("\n--- PALETTE ---")
    for color, hex_code in palette.items():
        print(f"{color}: {hex_code}")

    assert len(palette) == 5
    for i in range(1, 6):
        assert f"color-{i}" in palette
        assert palette[f"color-{i}"].startswith("#")

