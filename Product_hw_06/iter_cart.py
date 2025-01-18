class IterCart:
    def __init__(self, items, quantities):
        self.__items = items
        self.__quantities = quantities
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self.__items):
            item = self.__items[self._index]
            quantity = self.__quantities[self._index]
            self._index += 1
            return item, quantity
        else:
            raise StopIteration
