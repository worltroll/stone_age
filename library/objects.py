import arcade
from library.base import Launcher, Button
mw = Launcher(1255, 857, "Лаунчер")
b1 = Button(center_x=1255//2, center_y=300, scale=1, text='Начать игру')
mw.add_sprite(b1)