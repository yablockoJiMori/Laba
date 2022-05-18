from enum import Enum
from GameFilm import (
    game_film_write_to,
    game_film_read_from,
    GameFilm
)
from Cartoon import (
    cartoon_write_to,
    cartoon_read_from,
    Cartoon
)
from Documentary import (
    documentary_write_to,
    documentary_read_from,
    Documentary
)


class TypeFilm(Enum):
    game_film = 1
    cartoon = 2
    documentary = 3


class Film:
    def __init__(self):
        self.title = ""
        self.country = ""

        self.key = None
        self.obj = None


def film_read_from(stream, line):
    k = int(line)

    film = Film()
    film.title = stream.readline().rstrip("\n")

    match k:
        case 1:
            film.key = TypeFilm.game_film
            film.obj = GameFilm()
            game_film_read_from(film.obj, stream)

        case 2:
            film.key = TypeFilm.cartoon
            film.obj = Cartoon()
            cartoon_read_from(film.obj, stream)

        case 3:
            film.key = TypeFilm.documentary
            film.obj = Documentary()
            documentary_read_from(film.obj, stream)
            return film

        case _:
            return 0
    film.country = stream.readline().rstrip("\n")
    return film


def film_write_to(film, stream):
    match film.key:
        case TypeFilm.game_film:
            stream.write(f"Игровое кино.\n"
                         f"\tНазвание: {film.title}\n")
            game_film_write_to(film.obj, stream)

        case TypeFilm.cartoon:
            stream.write(f"Мультфильм.\n"
                         f"\tНазвание: {film.title}\n")
            cartoon_write_to(film.obj, stream)

        case TypeFilm.documentary:
            stream.write(f"Документальный фильм.\n"
                         f"\tНазвание: {film.title}\n")
            documentary_write_to(film.obj, stream)

        case _:
            stream.write("Некорректный фильм!\n")

    stream.write(f"\tСтрана: {film.country}\n")
