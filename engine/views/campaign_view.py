from engine.views.hud import HUDLayout

class CampaignView(arcade.View):
    def __init__(self):
        super().__init__()
        self.hud = None

    def setup(self):
        palette = {
            "color-1": arcade.color.GREEN,
            "color-2": arcade.color.MAGENTA,
            "color-3": arcade.color.WHITE,
            "color-4": arcade.color.BLACK,
            "color-5": arcade.color.PINK
        }
        self.hud = HUDLayout(self.window.width, self.window.height, palette)

    def on_draw(self):
        self.clear()
        self.hud.draw()

