# /engine/utils/color.py
def hex_to_rgb(hex_color):
    """Convierte un color en formato hexadecimal a una tupla RGB."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

