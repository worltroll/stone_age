import arcade


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)

    def setup(self):
        self.background_color = arcade.color.TEA_GREEN

    def on_draw(self):
        self.clear()