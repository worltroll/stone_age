import arcade

from library.objects import mw
from library.base import Launcher
from library.stone_age.base import Game



def main():
    launcher = Launcher()
    launcher.setup()

    game = Game()
    game.setup()

    window = arcade.Window(1255, 857, "Stone Age")
    window.show_view(launcher)

    arcade.run()


if __name__ == "__main__":
    main()