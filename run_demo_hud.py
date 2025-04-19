import arcade
from engine.views.hud import HUDLayout

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 720
SCREEN_TITLE = "HUD Visual Demo"

class DemoHUDView(arcade.View):
    def __init__(self):
        super().__init__()
        palette = {
            "color-1": arcade.color.GREEN,
            "color-2": arcade.color.MAGENTA,
            "color-3": arcade.color.WHITE,
            "color-4": arcade.color.BLACK,
            "color-5": arcade.color.PINK
        }
        self.hud = HUDLayout(SCREEN_WIDTH, SCREEN_HEIGHT, palette)

    def on_draw(self):
        self.clear()
        self.hud.draw()

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    demo_view = DemoHUDView()
    window.show_view(demo_view)
    arcade.run()

if __name__ == "__main__":
    main()

