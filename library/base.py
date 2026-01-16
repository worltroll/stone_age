import arcade
from arcade.gui import UIManager, UITextureButton, UITextArea, UILabel, UIStyleBase
from arcade.gui.widgets.layout import UIAnchorLayout, UIBoxLayout

from time import sleep

class Launcher(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.sprite_list = arcade.SpriteList()
        self.manager = UIManager()
        self.manager.enable()
        self.anchor_layout_left = UIAnchorLayout(x=-450, y=200)
        self.anchor_layout_main = UIAnchorLayout(y=-200)
        self.box_layout_main = UIBoxLayout(vertical=False, space_between=50)
        self.box_layout_left = UIBoxLayout(vertical=True, space_between=20)
        self.setup_widgets()

        self.anchor_layout_left.add(self.box_layout_left)
        self.anchor_layout_main.add(self.box_layout_main)
        self.manager.add(self.anchor_layout_main)
        self.manager.add(self.anchor_layout_left)
        self.width, self.height = width, height



    def setup(self):
        self.background_color = arcade.color.TEA_GREEN
        self.texture = arcade.load_texture('../images/L_background.jpg')



    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
    def clear_sprites(self):
        for sprite in self.sprite_list:
            sprite.remove_from_sprite_lists()


    def setup_widgets(self):

        wortroll_label = UITextArea(text='Wortroll \n games', x=900, y=650, font_size=50, text_color=arcade.color.RED, width=300, height=200)
        button_normal_texture = arcade.load_texture('../images/button.png')
        button_pressed_texture = arcade.load_texture('../images/button_pressed.png')
        button_hovered_texture = arcade.load_texture('../images/button_hovered.png')
        button_main1 = UITextureButton(texture=button_normal_texture, texture_pressed=button_pressed_texture,texture_hovered=button_hovered_texture, width=400, height=80, text='Начать игру')
        button_main2 = UITextureButton(texture=button_normal_texture, texture_hovered=button_hovered_texture, texture_pressed=button_pressed_texture, width=200,
                                       height=80, text='ЗАКРЫТЬ')
        button = UITextureButton(texture=button_normal_texture, texture_hovered=button_hovered_texture, texture_pressed=button_pressed_texture, width=300, height=80, text='ДОНАТ 10 РУБЛЕЙ')
        button1 = UITextureButton(texture=button_normal_texture, texture_hovered=button_hovered_texture, texture_pressed=button_pressed_texture,
                                 width=300, height=80, text='ДОНАТ 100 РУБЛЕЙ')
        button2 = UITextureButton(texture=button_normal_texture, texture_pressed=button_pressed_texture,texture_hovered=button_hovered_texture,
                                 width=300, height=80, text='ДОНАТ 1000 РУБЛЕЙ')
        button3 = UITextureButton(texture=button_normal_texture, texture_pressed=button_pressed_texture,texture_hovered=button_hovered_texture,
                                 width=300, height=80, text='ДОНАТ 10000 РУБЛЕЙ')
        button_main1.on_click = lambda event:self.add_sprite(arcade.Sprite(path_or_texture='../images/block.png', center_x=600, center_y=500, scale=10)) if len(self.sprite_list) ==0 else None
        button_main2.on_click = lambda event: self.clear_sprites()
        button1.on_click = lambda event: print("Вы задонатили 1рублей!!!")
        button2.on_click = lambda event: print("Вы задонатили 100 рублей!!!")
        button3.on_click = lambda event: print("Вы задонатили 1000 рублей!!!")
        button.on_click = lambda event: print("Вы задонатили 10000 рублей!!!")
        self.box_layout_main.add(button_main1)
        self.box_layout_main.add(button_main2)
        self.manager.add(wortroll_label)
        self.box_layout_left.add(button)
        self.box_layout_left.add(button1)
        self.box_layout_left.add(button2)
        self.box_layout_left.add(button3)

    def on_draw(self):
        self.clear()

        arcade.draw_texture_rect(self.texture, arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        self.sprite_list.draw()
        self.manager.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        pass




"""class Button(arcade.Sprite):
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
"""


def main():
    mw = Launcher(1255, 857, "Лаунчер")

    mw.setup()
    arcade.run()

if __name__ == "__main__":
    main()


