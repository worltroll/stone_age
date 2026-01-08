from environmental import Grass
from library.random_tools import random_coords
import random

import arcade


class Game(arcade.Window):
    def __init__(self, width, height, title, map_borders=[0, 600]):
        super().__init__(width, height, title, resizable=True)
        self.map_borders = map_borders

    def setup(self):
        self.generate_map()

        self.background_color = arcade.color.TEA_GREEN

    def on_draw(self):
        self.clear()

        self.grass_list.draw()

    def generate_map(self):
        self.generate_grass()

    def generate_grass(self):
        self.grass_list = arcade.SpriteList()
        for _ in range(1):
            self.grass_list.append(Grass(*random_coords(self.map_borders)))


def main():
    mw = Game(800, 600, "Каменный век")
    mw.setup()
    arcade.run()


if __name__ == "__main__":
    main()