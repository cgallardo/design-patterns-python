from typing import List


class Cart:
    def __init__(self, items: List,):
        self._items = items
        self._current_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_item > len(self._items) - 1:
            raise StopIteration
        else:
            self._current_item += 1

            return self._items[self._current_item - 1]


def main():
    cart = Cart([
        "Item 1",
        "Item 2",
        "Item 3",
        "Item 4",
        "Item 5",
        "Item 6"
    ])

    for item in cart:
        print(item)


if __name__ == "__main__":
    main()
