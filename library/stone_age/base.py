from environmental import Grass
import random

import arcade


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)

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
        for _ in range(10):
            self.grass_list.append(Grass(center_x=random.randint(0, self.width), center_y=random.randint(0, self.height)))


def main():
    mw = Game(800, 600, "Каменный век")
    mw.setup()
    arcade.run()


if __name__ == "__main__":
    main()