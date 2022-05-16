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
    stream.write(f"\tWay to create: {film.way_to_create.name}\n")
