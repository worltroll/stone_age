from random import randint


def random_coords(lst):
    return randint(*lst), randint(*lst)