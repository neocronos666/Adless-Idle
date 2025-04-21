from engine.utils.color import hex_to_rgb
import arcade

class HUDLayout:
    def __init__(self, width, height, theme_data):
        self.width = width
        self.height = height
        self.theme_data = theme_data

        self.palette = theme_data.get("palette", {})
        self.fonts = theme_data.get("fonts", {}).get("paths", {})
        self.layout = theme_data.get("hud", {}).get("layout", {})
        self.block_size = theme_data.get("hud", {}).get("block_size", {}) #ACAAAAAAAAAA

        self.elements = []
        self.labels = []
        self.progress_bar = None

        self.build_layout()

    def build_layout(self):
        w, h = self.width, self.height

        # Menu block (top-left)
        menu_color = self.palette.get("color-1", arcade.color.WHITE)

        self.elements.append(            
            arcade.draw_lbwh_rectangle_filled(
                w * 0.05, h * 0.95, w * 0.1, h * 0.08, hex_to_rgb(menu_color)
            )
        )
        self.labels.append(
            arcade.Text(
                "≡",
                w * 0.045,
                h * 0.935,
                hex_to_rgb(self.palette.get("color-3", arcade.color.BLACK)), #ACAAAA
                24,
                font_name=self.fonts.get("main", "Arial")
            )
        )

        # Progress bar (bottom center)
        bar_color = hex_to_rgb(self.palette.get("color-2", arcade.color.BLUE))
        bar_width, bar_height = self.block_size.get("progress_bar", [400, 20])
        self.progress_bar = arcade.SpriteSolidColor(bar_width, bar_height, bar_color)
        self.progress_bar.center_x = w / 2
        self.progress_bar.center_y = h * 0.05

    def draw(self):
        if self.elements:
            for element in self.elements:
                try:
                    if element:
                        element.draw()
                except AttributeError:
                    print("Advertencia: el elemento no tiene un método 'draw'.")

        if self.labels:
            for label in self.labels:
                try:
                    if label:
                        label.draw()
                except AttributeError:
                    print("Advertencia: la etiqueta no tiene un método 'draw'.")

        if self.progress_bar:
            try:
                if self.progress_bar and hasattr(self.progress_bar, "draw"):
                    self.progress_bar.draw()                
            except AttributeError:
                print("Advertencia: progress_bar no tiene un método 'draw'.")


'''
    def draw(self):
        for element in self.elements:
            element.draw()
        for label in self.labels:
            label.draw()
        if self.progress_bar:
            self.progress_bar.draw()

  
''' 

'''
import arcade

class HUDLayout:
    def __init__(self, width, height, palette):
        self.width = width
        self.height = height
        self.palette = palette

        # Elementos gráficos del HUD
        #self.elements = arcade.ShapeElementList()
        #self.elements = []
        self.elements = arcade.SpriteList()
        self.labels = []

        self.build_layout()

    def build_layout(self):
        w, h = self.width, self.height

        # Menú (esquina superior izquierda)
        menu_button = arcade.SpriteSolidColor(int(w * 0.1), int(h * 0.08), self.palette["color-1"])
        menu_button.center_x = w * 0.05
        menu_button.center_y = h * 0.95
        self.elements.append(menu_button)

        self.labels.append(arcade.Text("≡", w * 0.045, h * 0.935, self.palette["color-3"], 24))

        # Indicador de puntos (esquina superior derecha)
        self.labels.append(arcade.Text("Pts: 999", w * 0.75, h * 0.94, self.palette["color-3"], 18))

        # Botonera de entidades (izquierda)
        for i in range(5):
            button = arcade.SpriteSolidColor(int(w * 0.18), int(h * 0.08), self.palette["color-2"])
            button.center_x = w * 0.1
            button.center_y = h * (0.75 - i * 0.12)
            self.elements.append(button)

        # Panel INFO & UPGRADES (derecha centro)
        info_panel = arcade.SpriteSolidColor(int(w * 0.45), int(h * 0.6), self.palette["color-4"])
        info_panel.center_x = w * 0.7
        info_panel.center_y = h * 0.5
        self.elements.append(info_panel)

        self.labels.append(arcade.Text("Info / Upgrades", w * 0.48, h * 0.77, self.palette["color-3"], 14))

        # Barra inferior (opcional)
        self.progress_bar = arcade.SpriteSolidColor(int(w * 0.8), int(h * 0.04), self.palette["color-5"])
        self.progress_bar.center_x = w / 2
        self.progress_bar.center_y = h * 0.07
        self.elements.append(self.progress_bar)

    def draw(self):
        self.elements.draw()
        #self.progress_bar.draw()
        for label in self.labels:
            label.draw()


    def update(self):
        pass  # Para futuras animaciones o efectos dinámicos
'''
