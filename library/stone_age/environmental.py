import arcade


class Grass(arcade.Sprite):
    def __init__(self, center_x, center_y, **kwargs):
        super().__init__(filename='images/grass.png', center_x=center_x, center_y=center_y, **kwargs)