import arcade
from arcade.gui import UIManager, UITextureButton, UITextArea, UILabel, UIStyleBase
from arcade.gui.widgets.layout import UIAnchorLayout, UIBoxLayout
import json
class Game_Start(arcade.View):
    def __init__(self):
        super().__init__()
        self.pages = {'main': UIManager(), 'multiplayer': UIManager(), 'local': UIManager(), 'new_world_menu': UIManager()}
        self.sprite_list = arcade.SpriteList()
        self.page = 'main'
        self.pages[self.page].enable()
        self.anchor_layout_main = UIAnchorLayout(y=350)
        self.anchor_layout_local = UIAnchorLayout(y=0)
        self.anchor_layout_multiplayer = UIAnchorLayout(y=0)
        self.anchor_layout_new_world1 = UIAnchorLayout(y=200)
        self.anchor_layout_new_world2 = UIAnchorLayout(y=-200)

        self.box_layout_new_world1 = UIBoxLayout(vertical=False, space_between=100)
        self.box_layout_main = UIBoxLayout(vertical=False, space_between=100)
        self.box_layout_local = UIBoxLayout(vertical=True, space_between=50)
        self.box_layout_multiplayer = UIBoxLayout(vertical=True, space_between=50)
        self.box_layout_new_world2 = UIBoxLayout(vertical=False, space_between=100)

        self.setup_widgets()
        self.anchor_layout_main.add(self.box_layout_main)
        self.anchor_layout_local.add(self.box_layout_local)
        self.anchor_layout_multiplayer.add(self.box_layout_multiplayer)
        self.anchor_layout_new_world1.add(self.box_layout_new_world1)
        self.anchor_layout_new_world2.add(self.box_layout_new_world2)

        self.pages['new_world_menu'].add(self.anchor_layout_new_world1)
        self.pages['new_world_menu'].add(self.anchor_layout_new_world2)
        self.pages['main'].add(self.anchor_layout_main)
        self.pages['local'].add(self.anchor_layout_local)
        self.pages['multiplayer'].add(self.anchor_layout_multiplayer)

    def setup(self):
        self.background_color = arcade.color.TEA_GREEN
        self.texture = arcade.load_texture('images/L_background.jpg')

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def clear_sprites(self):
        for sprite in self.sprite_list:
            sprite.remove_from_sprite_lists()

    def change_page(self, page):
        self.pages[self.page].disable()
        self.page = page
        self.pages[self.page].enable()
    def new_world(self, world_name):
        data = {
            "fast_cells":[],
            "settings":{},
            "world_name":world_name
        }
        with open(f'saves/{world_name}.json', 'w') as nw:
            json.dump(data, nw)
            nw.close()

    def setup_widgets(self):
        arcade.load_font('fonts/OffBit-101.ttf')
        button_normal_texture = arcade.load_texture('images/button.png')
        button_pressed_texture = arcade.load_texture('images/button_pressed.png')
        button_hovered_texture = arcade.load_texture('images/button_hovered.png')
        # button style setting with UIStyle

        button_style = {
            'normal': UITextureButton.UIStyle(
                font_size=20,
                font_name=('OffBit 101'),
                font_color=arcade.color.BLACK

            ),
            'hover': UITextureButton.UIStyle(
                font_size=25,
                font_name=('OffBit 101'),
                font_color=arcade.color.GREEN

            ),
            'press': UITextureButton.UIStyle(
                font_size=20,
                font_name=('OffBit 101'),
                font_color=arcade.color.RED

            ),
            'disabled': UITextureButton.UIStyle(
                font_size=20,
                font_name=('OffBit 101'),
                font_color=arcade.color.GRAY

            )
        }
        button_multiplayer = UITextureButton(texture=button_normal_texture, texture_pressed=button_pressed_texture,
                                       texture_hovered=button_hovered_texture, width=300, height=80, text='Сетевая игра',
                                       style=button_style)

        button_local = UITextureButton(texture=button_normal_texture, texture_hovered=button_hovered_texture,
                                       texture_pressed=button_pressed_texture, width=300,
                                       height=80, text='Локальная игра', style=button_style)
        button_exit = UITextureButton(texture=button_normal_texture, texture_hovered=button_hovered_texture,
                                       texture_pressed=button_pressed_texture, width=200,
                                       height=80, text='Выход', style=button_style)
        button_menu = UITextureButton(texture=button_normal_texture, texture_hovered=button_hovered_texture,
                                       texture_pressed=button_pressed_texture, width=300,
                                       height=80, text='Главное меню', style=button_style)
        button_new_world = UITextureButton(texture=button_normal_texture, texture_hovered=button_hovered_texture,
                                           texture_pressed=button_pressed_texture, width=300,
                                           height=80, text='Создать новый мир', style=button_style)
        button_back = UITextureButton(texture=button_normal_texture, texture_hovered=button_hovered_texture,
                                           texture_pressed=button_pressed_texture, width=200,
                                           height=80, text='Назад', style=button_style)
        button_create = UITextureButton(texture=button_normal_texture, texture_hovered=button_hovered_texture,
                                           texture_pressed=button_pressed_texture, width=250,
                                           height=80, text='Создать', style=button_style)

        button_multiplayer.on_click = lambda event: self.change_page('multiplayer')
        button_local.on_click = lambda event: self.change_page('local')
        button_menu.on_click = lambda event: self.change_page('main')
        button_exit.on_click = lambda event: arcade.exit()
        button_new_world.on_click = lambda event: self.change_page('new_world_menu')
        button_back.on_click = lambda event: self.change_page('local')
        button_create.on_click = lambda event: self.new_world('test')
        self.box_layout_main.add(button_multiplayer)
        self.box_layout_main.add(button_local)
        self.box_layout_main.add(button_exit)


        self.box_layout_local.add(button_new_world)
        self.box_layout_local.add(button_menu)
        self.box_layout_new_world2.add(button_back)
        self.box_layout_new_world2.add(button_create)


        self.box_layout_multiplayer.add(button_menu)
    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.texture,
                                    arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        self.sprite_list.draw()
        self.pages[self.page].draw()
