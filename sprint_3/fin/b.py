# https://contest.yandex.ru/contest/23815/run-report/130876411/
"""
-- ПРИНЦИП РАБОТЫ --
Быстрая сортировка:
1) Определяем границы
2) Запускаем функцию замены элементов
    2.1) Определяем опорный элемент (использую половину, но можно любой)
    2.2) Двигаем указатели, если элемент "на своем месте"
    2.3) Доходим до элементов, которые нужно поменять и меняем
    2.4) В случае, если правый или левый равен опорному, двигаем противоположную
3) Рекурсивно вызываем по элементам ниже опорного
4) Рекурсивно вызываем по элементам выше опорного

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
В быстрой сортировке учитывается кажный элемент, так как рекурсивно вызывается строго разделенные по pivot

В функции swapping рассмотрим все варианты для левой границы (для правой условия зеркальны):
1) Граница выше опоры - элемент подходит для замены, ждем когда такой найдется справа. Если его нет, меняем с опорным
2) Граница ниже опоры - двигаем границу к следующему элементу (пока он ниже правой границы)
3) Граница равна опоре - меняем с правой границей и двигаем только противоположный индекс

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
На чтение O(n)

Сортировка:
На каждом уровне O(n/2) с предыдущего шага

На вывод O(n)

Итого:
В среднем случае - O(nlog(n))
В худшем случае - O(n**2) (когда в среднем элементе максимум или минимум)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(n) на хранение элементов
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


def swapping(nums, left, right):
    pivot = nums[(left + right) // 2]
    while left < right:
        if nums[left] > pivot:
            left += 1
            continue
        if nums[right] < pivot:
            right -= 1
            continue

        nums[left], nums[right] = nums[right], nums[left]

        if nums[right] == pivot:
            left += 1
        if nums[left] == pivot:
            right -= 1

    return left


def quick_sort(nums, start=0, end=None):
    left = start
    right = end - 1 if end is not None else len(nums) - 1
    if right - left < 1:
        return

    part_index = swapping(nums, left, right)

    quick_sort(nums, start=start, end=part_index)
    quick_sort(nums, start=part_index + 1, end=end)


if __name__ == '__main__':
    n = int(input())
    members = []
    for _ in range(n):
        name, done, failed = input().split()
        members.append(ContestResult(name, int(done), int(failed)))
    quick_sort(members)
    for member in members:
        print(member.name)
