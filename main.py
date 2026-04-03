import arcade

from launcher.base import Launcher
from game.base import Game



def main():
    launcher = Launcher(1255, 857)
    launcher.setup()

    game = Game(1346, 834)
    game.setup()

    window = arcade.Window(1255, 857, "Stone Age")
    window.show_view(launcher)

    arcade.run()


if __name__ == "__main__":
    main()