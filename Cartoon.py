import sys
from enum import Enum


class Cartoon:
    def __init__(self):
        self.way_to_create = None


class WayToCreate(Enum):
    drawn = 1
    puppet = 2
    plasticine = 3


def cartoon_read_from(film: Cartoon, stream):
    try:
        k = int(stream.readline())
    except Exception as e:
        stream.close()
        print("Ошибка преобразования типа объекта!")
        print(e)
        sys.exit(1)

    match k:
        case WayToCreate.drawn.value:
            film.way_to_create = WayToCreate.drawn
        case WayToCreate.puppet.value:
            film.way_to_create = WayToCreate.puppet
        case WayToCreate.plasticine.value:
            film.way_to_create = WayToCreate.plasticine
        case _:
            stream.close()
            print("Ошибка ключа типа данных!")
            sys.exit(1)


def cartoon_write_to(film: Cartoon, stream):
    try:
        k = film.way_to_create
    except Exception as e:
        stream.close()
        print("Ошибка преобразования типа объекта!")
        print(e)
        sys.exit(1)
    stream.write(f"\tСпособ создания: ")
    match k:
        case WayToCreate.drawn:
            stream.write(f"Нарисованный\n")
        case WayToCreate.puppet:
            stream.write(f"Кукольный \n")
        case WayToCreate.plasticine:
            stream.write(f"Пластилиновый\n")
        case _:
            stream.close()
            print("Ошибка ключа типа данных!")
            sys.exit(1)

