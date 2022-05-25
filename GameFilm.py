import sys


class GameFilm:
    def __init__(self):
        self.director = ""


def game_film_read_from(film: GameFilm, stream):
    try:
        film.director = stream.readline().rstrip("\n")
    except Exception as e:
        stream.close()
        print("Ошибка чтения игрового фильма!")
        print(e)
        sys.exit(1)


def game_film_write_to(film: GameFilm, stream):
    try:
        stream.write(f"\tРежиссер: {film.director}\n")
    except Exception as e:
        stream.close()
        print("Ошибка записи игрового фильма!")
        print(e)
        sys.exit(1)
