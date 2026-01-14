from environmental import Grass
from GUI import HotBar
from library.random_tools import random_coords

import arcade


class Game(arcade.Window):
    def __init__(self, width, height, title, map_borders=[0, 600]):
        super().__init__(width, height, title, resizable=True)
        self.map_borders = map_borders

    def setup(self):
        self.generate_map()
        self.hotbar = HotBar()
        self.background_color = arcade.color.TEA_GREEN

    def on_draw(self):
        self.clear()

        self.update_map()
        self.hotbar.update()
        self.hotbar.draw()

    def update_map(self):
        for i in self.environment:
            i.draw()

    def generate_map(self):
        self.environment = []
        self.generate_grass()

    def generate_grass(self):
        self.grass_list = arcade.SpriteList()
        for _ in range(1):
            self.grass_list.append(Grass(*random_coords(self.map_borders)))
        self.environment.append(self.grass_list)


if __name__ == "__main__":
    mw = Game(1346, 800, "Каменный век")
    mw.setup()
    arcade.run()
