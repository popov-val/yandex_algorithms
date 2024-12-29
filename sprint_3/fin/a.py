# https://contest.yandex.ru/contest/23815/run-report/130876294/
"""
-- ПРИНЦИП РАБОТЫ --
1) Получаем первый элемент "несломанного" массива, используя принцип бинарного поиска

2) Получается два отсортированных массива для поиска

3) Определяем в каком массиве может быть элемент

4) Ищем используя обычный бинарный поиск

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Так как добавление и извлечение проиходит по разным индексам и при каждом обращении происходит проверка
элементы никогда не перезапишут друг друга

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(log(N)) на поиск первого элемента
O(log(N)) на поиск искомого элемента
O(log(N)) + O(log(N)) ~ O(log(N))

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(1)
"""


def get_minimum_index(nums):
    left = 0
    right = len(nums) - 1
    while nums[left] > nums[right]:
        middle = (left + right) // 2
        if nums[middle] > nums[right]:
            left = middle + 1
        else:
            right = middle
    return left


def binary_search(nums, target, left, right):
    while left < right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif target < nums[middle]:
            right = middle
        else:
            left = middle + 1
    return -1


def broken_search(nums, target) -> int:
    minimum_index = get_minimum_index(nums)
    if nums[minimum_index] <= target <= nums[-1]:
        left = minimum_index
        right = len(nums)
    else:
        left = 0
        right = minimum_index

    return binary_search(nums, target, left, right)


def test():
    assert binary_search([1, 2, 3], 1, 0, 3) == 0
    assert binary_search([1, 2, 3], 3, 0, 3) == 2
    assert binary_search([1, 2, 3], 0, 0, 3) == -1
    assert binary_search([1, 2, 3], 4, 0, 3) == -1
    assert binary_search([1], 1, 0, 1) == 0
    assert binary_search([1], 2, 0, 1) == -1

    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6

    arr = [5, 1]
    assert broken_search(arr, 1) == 1

    arr = [34, 35, 37, 1]
    assert broken_search(arr, 3) == -1

    arr = [11, 19, 100, 101, 1]
    assert broken_search(arr, 101) == 3

    arr = [6, 7, 10, 0, 2, 4, 5]
    assert broken_search(arr, 3) == -1

    arr = [1]
    assert broken_search(arr, 1) == 0

    arr = [0, 1, 2]
    assert broken_search(arr, 1) == 1


if __name__ == '__main__':
    test()
