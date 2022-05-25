import sys


class Documentary:
    def __init__(self):
        self.year_of_issue = 0


def documentary_read_from(film: Documentary, stream):
    try:
        film.year_of_issue = int(stream.readline())
    except Exception as e:
        stream.close()
        print("Ошибка чтения документального фильма!")
        print(e)
        sys.exit(1)


def documentary_write_to(film: Documentary, stream):
    try:
        stream.write(f"\tГод выхода: {film.year_of_issue}\n")
    except Exception as e:
        stream.close()
        print("Ошибка записи документального фильма!")
        print(e)
        sys.exit(1)
