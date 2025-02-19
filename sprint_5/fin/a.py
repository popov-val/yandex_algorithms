# https://contest.yandex.ru/contest/24810/run-report/133473957/
"""
-- ПРИНЦИП РАБОТЫ --
1) Чтение
2) Добавление в кучу
    2.1) Добавляем к списку
    2.2) Просеиваем вверх
3) Получение из кучи
    2.1) Берем первый элемент
    2.2) Меням первый на последний
    2.3) Просеиваем вниз
4) Вывод

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Благодаря свойствам кучи и алгоритму "просеивания" достигается сортировка

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(NlogN) - на добавление в кучу (просеивание)
O(NlogN) - на вывод из кучи (просеивание)

Итого: O(NlogN) + O(NlogN)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(N) - на кучу
"""


class ContestResult:
    def __init__(self, name, done, failed):
        self.name = name
        self.done = done
        self.failed = failed

    def __lt__(self, other):
        if self.done != other.done:
            return self.done < other.done
        if self.failed != other.failed:
            return self.failed > other.failed
        return self.name > other.name

    def __str__(self):
        return self.name


class Heap:
    def __init__(self):
        self._heap = [None]

    def __str__(self):
        return f'Heap({self._heap})'

    def __bool__(self):
        return len(self._heap) > 1

    def sift_up(self, idx=None):
        idx = len(self._heap) - 1 if not idx else idx
        if idx == 1:
            return
        parent_id = idx // 2
        if self._heap[idx] > self._heap[parent_id]:
            self._heap[idx], self._heap[parent_id] = self._heap[parent_id], self._heap[idx]
            self.sift_up(parent_id)

    def sift_down(self, idx=None):
        idx = 1 if not idx else idx
        left_child = idx * 2
        right_child = idx * 2 + 1
        ids = [idx, left_child, right_child]
        exists_els = [self._heap[id_] for id_ in ids if id_ < len(self._heap)]
        max_el = max(exists_els)
        if max_el == self._heap[idx]:
            return
        if max_el == self._heap[left_child]:
            self._heap[left_child], self._heap[idx] = self._heap[idx], self._heap[left_child]
            self.sift_down(left_child)
            return
        if max_el == self._heap[right_child]:
            self._heap[right_child], self._heap[idx] = self._heap[idx], self._heap[right_child]
            self.sift_down(right_child)
            return

    def add(self, el):
        self._heap.append(el)
        self.sift_up()

    def get(self):
        res = self._heap[1]
        last = self._heap.pop()
        if self:
            self._heap[1] = last
            self.sift_down()
        return res


if __name__ == '__main__':
    heap = Heap()
    n = int(input())
    for _ in range(n):
        name, done, failed = input().split()
        heap.add(ContestResult(name, int(done), int(failed)))

    while heap:
        print(heap.get())
