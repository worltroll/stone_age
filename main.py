import arcade

from launcher.base import Launcher
from game.base import Game
from game_start_menu.base import Game_Start


class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=False)


def main():
    mw = Window(1346, 834, "Каменный век")

    game = Game(1346, 834)
    gs = Game_Start()
    launcher = Launcher(1255, 857)

    game.launcher_view = launcher
    game.setup()
    gs.setup()
    launcher.setup()

    mw.show_view(launcher)
    arcade.run()


if __name__ == "__main__":
    main()
