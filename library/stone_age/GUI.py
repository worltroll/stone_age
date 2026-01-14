import arcade


class Cell(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=1, **kwargs):
        super().__init__(path_or_texture='../../images/cell.png', scale=scale, center_x=center_x, center_y=center_y,
                         **kwargs)
        self.is_selected = False

    def update(self):
        if self.is_selected:
            self.path_or_texture = '../../images/selected_cell.png'
        else:
            self.path_or_texture = '../../images/cell.png'


class HotBar(arcade.SpriteList):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.selected_cell_id = 1
        for i in range(10):
            self.append(Cell(97 + 128 * i, 97))
        self[self.selected_cell_id].is_selected = True

    def update(self):
        for i in self:
            i.update()