from environmental import Grass
from GUI import HotBar, Inventory
from library.random_tools import random_coords

import arcade


class Game(arcade.View):
    def __init__(self, width, height, map_borders=[0, 600]):
        super().__init__()
        self.map_borders = map_borders

    def setup(self):
        self.generate_map()
        self.hotbar = HotBar()
        self.inventory = Inventory()
        self.background_color = arcade.color.TEA_GREEN

        self.speed = 3

        self.inventory_flag = False
        self.up_flag = False
        self.left_flag = False
        self.down_flag = False
        self.right_flag = False

    def on_draw(self):
        self.clear()

        self.update_map()
        self.hotbar.update()
        self.hotbar.draw()

        if self.inventory_flag:
            self.inventory.draw()

    def on_key_press(self, symbol, modifiers):
        match symbol:
            case arcade.key.KEY_1:
                self.hotbar.select(0)
            case arcade.key.KEY_2:
                self.hotbar.select(1)
            case arcade.key.KEY_3:
                self.hotbar.select(2)
            case arcade.key.KEY_4:
                self.hotbar.select(3)
            case arcade.key.KEY_5:
                self.hotbar.select(4)
            case arcade.key.KEY_6:
                self.hotbar.select(5)
            case arcade.key.KEY_7:
                self.hotbar.select(6)
            case arcade.key.KEY_8:
                self.hotbar.select(7)
            case arcade.key.KEY_9:
                self.hotbar.select(8)
            case arcade.key.KEY_0:
                self.hotbar.select(9)
            case arcade.key.E:
                self.inventory_flag = not self.inventory_flag
            case arcade.key.W:
                self.up_flag = not self.up_flag
            case arcade.key.A:
                self.left_flag = not self.left_flag
            case arcade.key.S:
                self.down_flag = not self.down_flag
            case arcade.key.D:
                self.right_flag = not self.right_flag

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
    mw = Window(1346, 834, "Каменный век")
    game = Game(1346, 834)
    game.setup()
    mw.show_view(game)
    arcade.run()
