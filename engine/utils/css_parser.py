# engine/utils/css_parser.py

import re

def parse_palette_css(path, mode="dark"):
    with open(path, "r") as f:
        css = f.read()

    # Seleccionar solo el bloque de modo deseado
    pattern = rf"--color-(\d)-{mode}:\s*(#[a-fA-F0-9]{6});"
    matches = re.findall(pattern, css)

    if not matches:
        return {
            "color-1": "#ffffff",
            "color-2": "#cccccc",
            "color-3": "#999999",
            "color-4": "#666666",
            "color-5": "#333333"
        }

    palette = {f"color-{key}": value for key, value in matches}
    return palette

