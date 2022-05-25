import sys
from film import (
    film_write_to,
    film_read_from,
    check_films,
    Film

)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = self


class DList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


def dlist_push_back(dlist: DList, item):
    node = Node(item)

    if dlist.size == 0:
        dlist.head = node
        dlist.tail = node
        dlist.size += 1
        return

    dlist.tail.next = node
    node.next = dlist.head
    dlist.tail = node

    dlist.size += 1


def dlist_clear(dlist: DList):
    dlist.head = None
    dlist.tail = None
    dlist.size = 0


def num_vowels(string) -> int:
    vowels = set("aeiouауоыиэяюёеAEIOUАУОЫИЭЯЮЁЕ")
    amount = 0
    for letter in string:
        if letter in vowels:
            amount += 1
    return amount


def dlist_read_from(dlist: DList, stream):
    while line := stream.readline():
        item = film_read_from(stream, line)
        dlist_push_back(dlist, item)


def dlist_write_to(dlist: DList, stream):
    stream.write(f"В контейнере {dlist.size} элементов.\n")

    current_item = dlist.head
    if dlist.size != 0:
        try:
            film_write_to(current_item.data, stream)
            stream.write(f"\tКоличество гласных: {num_vowels(current_item.data.title)}\n")
        except Exception as e:
            stream.close()
            print("Ошибка записи фильма!")
            print(e)
            sys.exit(1)
        current_item = current_item.next
        while current_item is not dlist.head:
            try:
                film_write_to(current_item.data, stream)
                stream.write(f"\tКоличество гласных: {num_vowels(current_item.data.title)}\n")
            except Exception as e:
                stream.close()
                print("Ошибка записи фильма!")
                print(e)
                sys.exit(1)
            current_item = current_item.next


def match(first, second) -> bool:
    return num_vowels(first.title) < num_vowels(second.title)


def dlist_sort(dlist: DList):
    for i in range(dlist.size):
        curr_node = dlist.head
        while curr_node.next != dlist.head:
            next_node = curr_node.next
            if match(curr_node.data, next_node.data):
                curr_node.data, next_node.data = next_node.data, curr_node.data
            curr_node = next_node


def dlist_write_game_film_to(dlist: DList, stream):
    from film import TypeFilm
    stream.write("Только игровые фильмы.\n")
    current_item = dlist.head
    if dlist.size != 0:
        if current_item.data.key == TypeFilm.game_film:
            try:
                film_write_to(current_item.data, stream)
                stream.write(f"\tКоличество гласных: {num_vowels(current_item.data.title)}\n")
            except Exception as e:
                stream.close()
                print("Ошибка записи фильма!")
                print(e)
                sys.exit(1)
        current_item = current_item.next
        while current_item is not dlist.head:
            if current_item.data.key == TypeFilm.game_film:
                try:
                    film_write_to(current_item.data, stream)
                    stream.write(f"\tКоличество гласных: {num_vowels(current_item.data.title)}\n")
                except Exception as e:
                    stream.close()
                    print("Ошибка записи фильма!")
                    print(e)
                    sys.exit(1)
            current_item = current_item.next

def dlist_check_films(dlist: DList):
    film_items = []

    current_node = dlist.head
    film: Film = current_node.data
    film_items.append(film)
    current_node = current_node.next
    while current_node is not dlist.head:
        film: Film = current_node.data
        film_items.append(film)
        current_node = current_node.next

    film_items_2 = film_items.copy()

    for film_1 in film_items:
        for film_2 in film_items_2:
            check_films(film_1, film_2)
