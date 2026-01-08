import arcade


class Cell(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=1, **kwargs):
        super().__init__(path_or_texture='../../images/cell.png', scale=scale, center_x=center_x, center_y=center_y,
                         **kwargs)
        self.is_selected = False

    def update(self):
        if self.is_selected:
            self.path_or_texture = '../../images/selected_cell.png'
