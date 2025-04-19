import sys
import os
import pytest
import arcade

# Agrega la raíz del proyecto al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine.views.hud import HUDLayout

@pytest.fixture(scope="module", autouse=True)
def arcade_window():
    window = arcade.Window(720, 1280, "Test Window", visible=False)
    yield
    window.close()

@pytest.fixture
def test_palette():
    return {
        "color-1": arcade.color.GREEN,
        "color-2": arcade.color.MAGENTA,
        "color-3": arcade.color.WHITE,
        "color-4": arcade.color.BLACK,
        "color-5": arcade.color.PINK
    }

def test_hud_layout_initialization(test_palette):
    width = 720
    height = 1280

    hud = HUDLayout(width, height, test_palette)

    assert len(hud.elements) >= 6
    assert len(hud.labels) >= 2
    assert callable(hud.draw)
    assert callable(hud.update)


'''
import sys
import os
import pytest
import arcade

# Agregar la raíz del proyecto al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine.views.hud import HUDLayout

@pytest.fixture
def test_palette():
    return {
        "color-1": arcade.color.GREEN,
        "color-2": arcade.color.MAGENTA,
        "color-3": arcade.color.WHITE,
        "color-4": arcade.color.BLACK,
        "color-5": arcade.color.PINK
    }

def test_hud_layout_initialization(test_palette):
    # Simular dimensiones estándar (ej: resolución vertical 720p)
    width = 720
    height = 1280

    # Crear el layout
    hud = HUDLayout(width, height, test_palette)

    # Verificar que se crearon los bloques principales
    assert len(hud.elements) >= 6, "Debería haber al menos 6 elementos gráficos"
    assert len(hud.labels) >= 2, "Debería haber al menos 2 etiquetas de texto"

    # Verificar que los métodos draw y update existen
    assert callable(hud.draw)
    assert callable(hud.update)
'''
