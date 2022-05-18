import sys

from container import (
    dlist_read_from,
    dlist_write_to,
    dlist_clear,
    dlist_write_game_film_to,
    DList
)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("incorrect command line! \n"
              "Waited: command in_file out_file")
        sys.exit(1)

    input_file = open(sys.argv[1], "r", encoding="utf-8")
    output_file = open(sys.argv[2], "w", encoding="utf-8")

    print("Старт")

    container = DList()
    dlist_read_from(container, input_file)

    print("Файл прочитан.")
    dlist_write_to(container, output_file)
    dlist_write_game_film_to(container, output_file)

    dlist_clear(container)
    print("Контейнер отчищен.")

    dlist_write_to(container, output_file)
    print("Стоп")

    input_file.close()
    output_file.close()


