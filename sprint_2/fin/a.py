# https://contest.yandex.ru/contest/22781/run-report/130109149/
"""
-- ПРИНЦИП РАБОТЫ --
Как указано в условии задачи, реализован дек на основе кольцевого буфера
Добавление в конец происходит слева на право
Добавление в начало происходит справо на лево

Голова и хвост элементов опеределяется по разным индексам head для forward и tail для back

Методы push_* и pop_* объедененны так как логика добавления и извлечения схожа


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Так как добавление и извлечение проиходит по разным индексам и при каждом обращении происходит проверка
элементы никогда не перезапишут друг друга

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(1) так как мы сохраняются текущии позиции

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(N) так как сохраняем элементы

"""

class Deck:
    def __init__(self, size):
        self.max_size = size
        self.items = [None] * size
        self.head = -1
        self.tail = 0
        self._size = 0

    def _push(self, value, index_name):
        if self._size == self.max_size:
            return 'error'
        index = getattr(self, index_name)
        self.items[index] = value
        next_index = (index + 1 if index_name == 'tail' else index - 1) % self.max_size
        setattr(self, index_name, next_index)
        self._size += 1

    def push_back(self, value):
        return self._push(value, 'tail')

    def push_front(self, value):
        return self._push(value, 'head')

    def _pop(self, index_name):
        if self._size == 0:
            return 'error'
        index = getattr(self, index_name)
        next_index = (index - 1 if index_name == 'tail' else index + 1) % self.max_size
        el = self.items[next_index]
        self.items[next_index] = None
        setattr(self, index_name, next_index)
        self._size -= 1
        return el

    def pop_front(self):
        return self._pop('head')

    def pop_back(self):
        return self._pop('tail')

    def __str__(self):
        return f'Deck({str(self.items)})'


if __name__ == '__main__':
    n = int(input())
    size = int(input())
    d = Deck(size)
    for i in range(n):
        command, *args = input().split()
        if args:
            args = [int(el) for el in args]
        method = getattr(d, command)
        output = method(*args)
        if output is not None:
            print(output)
