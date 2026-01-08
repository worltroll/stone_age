import arcade


class Grass(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=1,  **kwargs):
        super().__init__(path_or_texture='../../images/grass.png', scale=scale, center_x=center_x, center_y=center_y, **kwargs)