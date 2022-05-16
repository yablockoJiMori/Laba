class GameFilm:
    def __init__(self):
        self.director = ""


def game_film_read_from(film: GameFilm, stream):
    film.director = stream.readline().rstrip("\n")

def game_film_write_to(film: GameFilm, stream):
    stream.write(f"\tDirector: {film.director}\n")
