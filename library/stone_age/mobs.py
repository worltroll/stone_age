import arcade


class Mob(arcade.Sprite):
    def __init__(self, path_or_texture, center_x, center_y, scale=1, **kwargs):
        super().__init__(path_or_texture=path_or_texture, scale=scale, center_x=center_x, center_y=center_y, **kwargs)


class People(Mob):
    def __init__(self, path_or_texture, center_x, center_y, scale=1, **kwargs):
        super().__init__(path_or_texture=path_or_texture, scale=scale, center_x=center_x, center_y=center_y, **kwargs)


class Player(People):
    def __init__(self, center_x, center_y, scale=1, **kwargs):
        super().__init__(path_or_texture='./../images/people', scale=scale, center_x=center_x, center_y=center_y, **kwargs)