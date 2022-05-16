from enum import Enum

class Cartoon:
    def __init__(self):
        self.way_to_create = None

class WayToCreate(Enum):
    drawn = 1
    puppet = 2
    plasticine = 3

def cartoon_read_from(film: Cartoon, stream):
    k = int(stream.readline())

    match k:
        case WayToCreate.drawn.value:
            film.way_to_create = WayToCreate.drawn
        case WayToCreate.puppet.value:
            film.way_to_create = WayToCreate.puppet
        case WayToCreate.plasticine.value:
            film.way_to_create = WayToCreate.plasticine
        case _:
            return 0


def cartoon_write_to(film: Cartoon, stream):
    k = film.way_to_create
    stream.write(f"\tСпособ создания: ")
    match k:
        case WayToCreate.drawn:
            stream.write(f"Нарисованный\n")
        case WayToCreate.puppet:
            stream.write(f"Кукольный \n")
        case WayToCreate.plasticine:
            stream.write(f"Пластилиновый\n")
        case _:
            return 0

