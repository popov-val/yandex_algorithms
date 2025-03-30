# https://contest.yandex.ru/contest/25070/run-report/135651061/
"""
-- ПРИНЦИП РАБОТЫ --
Карту можно вопринимать как пронумерованную "таблицу"
Как пример:
3 3
#.#      1 2 3
.#.  ->  4 5 6
#.#      7 8 9
Получается для обращения по индексам к карте:
i = num // m
j = num % m
где num номер точки из таблицы
Таким образом смещение можно считать добавлением 1 для соседей справа(слева) и m для соседей сверху(снизу)

К сожалению, у меня решение близкое к сохранению координат не прошло:
https://contest.yandex.ru/contest/25070/run-report/135648078/


1) Читаем данные и подготавливаем структуры:
    - cnt счетчик земли
    - max_size максимальный размер земли
    - shifts сдиги для перемещения по соседям
    - plate карта
    - d - очередь для прохождения по соседям
    - nums количество точек
    - visited массив посещенных точек
    - next_v - следующая точка
2) Двигаемся начиная с первой точки пока номер не превысит передел
    Получаем из номера индексы
    Если точка посещена или там вода, то двигаемся к следующей точке
    Помечаем как посещенную и увеличиваем счетчик
3) Обрабатываем соседей
    Проходимся по каждому сдвигу и добавляем
    Проверяем, что такая точка существует и сдвиг корректный
    Если эта точка следующая к рассмотрению, увеличиваем следующаюю точку
    Если это земля, то добавляем к обходу
4) Считаем максимум

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Используя номера и массив посещенных вершин, обработка каждой точки гарантированно


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(N*M) - на каждую точку, так как если точна уже посещена мы двигали рассматриваемую вершину

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(N*M) на массив с флагами о посещениях
"""

from collections import deque


def process_neighbors(next_v, visited, shifts, nums, m, plate):
    d = deque()
    d.append(next_v)
    visited[next_v] = True
    next_v += 1
    size = 0
    while d:
        num = d.popleft()
        size += 1
        for shift in shifts:
            neib = num + shift
            # Проверка на наличие соседа
            if neib < 0 or neib >= nums:
                continue
            # Проверям что сосед справа/слева находится на той же строке
            if shift in [-1, 1] and neib // m != num // m:
                continue
            if visited[neib]:
                continue
            visited[neib] = True
            next_v += next_v == neib
            if plate[neib // m][neib % m] == '#':
                d.append(neib)
    return size, next_v


def main():
    cnt = 0
    max_size = 0
    n, m = list(map(int, input().split()))
    shifts = [1, -1, m, -m]
    plate = [input() for _ in range(n)]
    nums = n * m
    visited = [False for _ in range(nums)]
    next_v = 0
    while next_v < nums:
        i = next_v // m
        j = next_v % m
        if visited[next_v]:
            next_v += 1
            continue
        if plate[i][j] == '.':
            visited[next_v] = True
            next_v += 1
            continue

        cnt += 1
        size, next_v = process_neighbors(next_v, visited, shifts, nums, m, plate)

        max_size = max(size, max_size)
    return cnt, max_size


if __name__ == '__main__':
    print(*main())
