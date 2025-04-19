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

