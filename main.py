import arcade
from library.base import Launcher
from library.stone_age.base import Game


def main():
    mw = Launcher(800, 600, "Лаунчер")
    mw.setup()
    arcade.run()


if __name__ == "__main__":
    main()