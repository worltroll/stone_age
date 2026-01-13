import arcade
from time import sleep

class Launcher(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.sprite_list = arcade.SpriteList()
        self.width, self.height = width, height
    def setup(self):
        self.background_color = arcade.color.TEA_GREEN
        self.texture = arcade.load_texture('../images/L_background.jpg')
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.texture, arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        self.sprite_list.draw()

        for i in self.sprite_list:
            try:
                i.draw_text()
            except:
                pass

    def on_mouse_press(self, x, y, button, modifiers):
        pushed_button = arcade.get_sprites_at_point((x, y), self.sprite_list)
        for button in pushed_button:

                button.on_press()




class Button(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=1, text='test', command=None, **kwargs):
        super().__init__(path_or_texture='../images/button.png', scale=scale, center_x=center_x, center_y=center_y,
                         **kwargs)
        self.text = arcade.Text(text, center_x-75*scale, center_y - 20, arcade.color.BLACK, 50)
        self.command = command

    def on_press(self, *args):
        self.command(*args)

    def draw_text(self):
        self.text.draw()



def command():
    print('test')


def main():
    mw = Launcher(1255, 857, "Лаунчер")
    b1 = Button(center_x=1255//2, center_y=300, scale=2, text='Начать игру', command=command())
    mw.add_sprite(b1)

    mw.setup()
    arcade.run()

if __name__ == "__main__":
    main()


