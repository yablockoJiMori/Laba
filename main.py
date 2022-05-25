import sys

from container import (
    dlist_read_from,
    dlist_write_to,
    dlist_clear,
    dlist_sort,
    dlist_write_game_film_to,
    dlist_check_films,
    DList
)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Ошибка. Ожидалось принять файлы ввода и вывода.")
        sys.exit(1)

    try:
        input_file = open(sys.argv[1], "r", encoding="utf-8")
    except OSError:
        print(f"Ошибка открытия файла {sys.argv[1]}")
        sys.exit(1)

    try:
        output_file = open(sys.argv[2], "w", encoding="utf-8")
    except OSError:
        input_file.close()
        print(f"Ошибка открытия файла {sys.argv[2]}")
        sys.exit(1)

    print("Старт")

    container = DList()
    dlist_read_from(container, input_file)
    dlist_write_to(container, output_file)
    print("Файл прочитан.")
    dlist_check_films(container)
    print("Сравнение завершено")
    dlist_sort(container)
    dlist_write_to(container, output_file)
    dlist_write_game_film_to(container, output_file)

    dlist_clear(container)
    print("Контейнер отчищен.")

    dlist_write_to(container, output_file)
    print("Стоп")

    input_file.close()
    output_file.close()


