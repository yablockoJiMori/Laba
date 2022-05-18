from film import (
    film_write_to,
    film_read_from,

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
        film_write_to(current_item.data, stream)
        stream.write(f"\tКоличество гласных: {num_vowels(current_item.data.title)}\n")
        current_item = current_item.next
        while current_item is not dlist.head:
            film_write_to(current_item.data, stream)
            stream.write(f"\tКоличество гласных: {num_vowels(current_item.data.title)}\n")
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
