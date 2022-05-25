import sys
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
    try:
        k = int(line)
    except Exception as e:
        stream.close()
        print("Ошибка преобразования типа объекта!")
        print(e)
        sys.exit(1)

    film = Film()
    try:
        film.title = stream.readline().rstrip("\n")
    except Exception as e:
        stream.close()
        print("Ошибка чтения названия фильма!")
        print(e)
        sys.exit(1)

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

        case _:
            stream.close()
            print(f"Введен неверный тип объекта: {k}")
            sys.exit(1)

    try:
        film.country = stream.readline().rstrip("\n")
    except Exception as e:
        stream.close()
        print("Ошибка чтения страны!")
        print(e)
        sys.exit(1)
    return film


def film_write_to(film, stream):
    try:
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
                stream.close()
                print("Ошибка ключа типа данных!")
                sys.exit(1)
    except Exception as e:
        stream.close()
        print("Ошибка записи данных в файл!")
        print(e)
        sys.exit(1)

    try:
        stream.write(f"\tСтрана: {film.country}\n")
    except Exception as e:
        stream.close()
        print("Ошибка записи страны в файл!")
        print(e)
        sys.exit(1)


def check_films(film_1, film_2):
    match film_1.obj, film_2.obj:
        case GameFilm(), GameFilm():
            print("Фильмы из одной категории.")
            print("Категория - первый фильм: Игровой, второй фильм: Игровой")
            print(f"Название - первый фильм: {film_1.title}, второй фильм: {film_2.title}")
            print()

        case GameFilm(), Cartoon():
            print("Фильмы из разных категорий.")
            print("Категория - первый фильм: Игровой, второй фильм: Мультфильм")
            print(f"Название - первый фильм: {film_1.title}, второй фильм: {film_2.title}")
            print()

        case GameFilm(), Documentary():
            print("Фильмы из разных категорий.")
            print("Категория - первый фильм: Игровой, второй фильм: Документальный")
            print(f"Название - первый фильм: {film_1.title}, второй фильм: {film_2.title}")
            print()

        case Cartoon(), GameFilm():
            print("Фильмы из разных категорий.")
            print("Категория - первый фильм: Мультфильм, второй фильм: Игровой")
            print(f"Название - первый фильм: {film_1.title}, второй фильм: {film_2.title}")
            print()

        case Cartoon(), Cartoon():
            print("Фильмы из одной категории.")
            print("Категория - первый фильм: Мультфильм, второй фильм: Мультфильм")
            print(f"Название - первый фильм: {film_1.title}, второй фильм: {film_2.title}")
            print()

        case Cartoon(), Documentary():
            print("Фильмы из разных категорий.")
            print("Категория - первый фильм: Мультфильм, второй фильм: Документальный")
            print(f"Название - первый фильм: {film_1.title}, второй фильм: {film_2.title}")
            print()

        case Documentary(), GameFilm():
            print("Фильмы из разных категорий.")
            print("Категория - первый фильм: Документальный, второй фильм: Игровой")
            print(f"Название - первый фильм: {film_1.title}, второй фильм: {film_2.title}")
            print()

        case Documentary(), Cartoon():
            print("Фильмы из разных категорий.")
            print("Категория - первый фильм: Документальный, второй фильм: Мультфильм")
            print(f"Название - первый фильм: {film_1.title}, второй фильм: {film_2.title}")
            print()

        case Documentary(), Documentary():
            print("Фильмы из одной категории.")
            print("Категория - первый фильм: Документальный, второй фильм: Документальный")
            print(f"Название - первый фильм: {film_1.title}, второй фильм: {film_2.title}")
            print()
