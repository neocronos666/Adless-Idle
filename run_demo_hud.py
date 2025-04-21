# run_demo_hud.py
import arcade
from theme_loader import ThemeLoader
from engine.views.hud import HUDLayout

class DemoHUDApp(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.hud = None


    def setup(self):
        theme = ThemeLoader(debug=True).get_theme_data()
        self.hud = HUDLayout(self.width, self.height, theme)

    def on_draw(self):
        #arcade.start_render()
        self.clear()
        if self.hud:
            self.hud.draw()

    def on_update(self, delta_time):
        pass


def main():
    window = DemoHUDApp(720, 1000, "Adless Idle - HUD Demo")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()



'''
import arcade
from engine.views.hud import HUDLayout
from theme_loader import ThemeLoader

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 720
SCREEN_TITLE = "HUD Visual Demo"

theme = ThemeLoader(debug=True).get_theme_data()
hud = HUDLayout(SCREEN_WIDTH, SCREEN_HEIGHT, theme)


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
'''
