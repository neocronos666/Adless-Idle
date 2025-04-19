import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ejemplo básico con Arcade 3.x"

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.mouse_over_button = False

    def on_draw(self):
        self.clear()
        # Simula un botón con `draw_lrbt_rectangle_filled`
        color = arcade.color.BLUE if self.mouse_over_button else arcade.color.DARK_BLUE
        arcade.draw_lrbt_rectangle_filled(300, 500, 275, 325, color)
        arcade.draw_text("¡Clickeame!", 400, 290,
                         arcade.color.WHITE, 16, anchor_x="center", anchor_y="center")

        arcade.draw_text("Bienvenido a tu app con Arcade!",
                         200, 500, arcade.color.BLACK, 20)

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_over_button = 300 <= x <= 500 and 275 <= y <= 325

    def on_mouse_press(self, x, y, button, modifiers):
        if self.mouse_over_button:
            print("🎉 ¡Botón presionado!")

if __name__ == "__main__":
    game = MyGame()
    arcade.run()

