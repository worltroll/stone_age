import arcade


class Launcher(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.sprite_list = arcade.SpriteList()
    def setup(self):
        self.background_color = arcade.color.TEA_GREEN
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
    def on_draw(self):
        self.clear()
        self.sprite_list.draw()
        for i in self.sprite_list:
            try:
                i.draw_text()
            except:
                pass


class Button(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=1, text = 'test',command=None,  **kwargs):
        super().__init__(path_or_texture='../images/button.png', scale=scale, center_x=center_x, center_y=center_y, **kwargs)
        self.text = arcade.Text(text, center_x-50, center_y-20, arcade.color.BLACK, 50)
        self.command = command
    def command(self, *args):
        self.command(*args)
    def draw_text(self):
        self.text.draw()
def main():
    mw = Launcher(1346, 800, "Каменный век лаунчер")
    button1 = Button(center_x=500, center_y=500, scale=1, text='test')
    mw.add_sprite(button1)
    mw.setup()
    arcade.run()


if __name__ == "__main__":
    main()
