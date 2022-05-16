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




class TypeFilm(Enum):
    game_film = 1
    cartoon = 2


class Film:
    def __init__(self):
        self.title = ""

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
            return film

        case 2:
            film.key = TypeFilm.cartoon
            film.obj = Cartoon()
            cartoon_read_from(film.obj, stream)
            return film

        case _:
            return 0


def film_write_to(film, stream):
    match film.key:
        case TypeFilm.game_film:
            stream.write(f"This is a game movie.\n"
                         f"\tTitle: {film.title}\n")
            game_film_write_to(film.obj, stream)

        case TypeFilm.cartoon:
            stream.write(f"This is a cartoon.\n"
                         f"\tTitle: {film.title}\n")
            cartoon_write_to(film.obj, stream)

        case _:
            stream.write("Incorrect film!\n")
