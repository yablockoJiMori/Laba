class Documentary:
    def __init__(self):
        self.year_of_issue = 0


def documentary_read_from(film: Documentary, stream):
    film.year_of_issue = int(stream.readline())


def documentary_write_to(film: Documentary, stream):
    stream.write(f"\tГод выхода: {film.year_of_issue}\n")