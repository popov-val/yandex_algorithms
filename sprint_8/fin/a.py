# https://contest.yandex.ru/contest/26133/run-report/136939940/
"""
-- ПРИНЦИП РАБОТЫ --
1) Читаем данные
2) Распаковываем
    - Проверяем на наличие строки
    - Получаем следущее число (перед распаковкой)
    - Если его нет значит строку не надо распаковывать
    - Если есть записываем число и находим закрывающую скобку
    - Рекурсивно обрабатываем внутренее выражение слева и справа
    - Конкатенируем
3) Считаем максимальный префикс
    - Проходимся по каждому символу каждой строки

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Распаковка:
Если числа нет, значит и скобок нет, значит строку распаковывать не нужно

Если число есть, значит следующий символ открывающая строка, нахождение закрывающей через стэк

Получение префикса:
Наивный алгоритм, фактически просто проходимся по всем

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
N - длина строки
M - кол-во строк
Распаковка: O(N*M)
Нахождение префикса: O(N*M)
Итого: O(N*M) + O(N*M) ~ O(N*M)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Распаковка: O(N/3) (худший случай, когда почти вся строка в скобках). 2[2[2[a]]]
Нахождение префикса: O(const)
На сами строки: O(N*M)
Итого: O(N*M) + O(N/3) + O(const) ~ O(N*M)
"""


def get_next_bra_id(s, start):
    i = start
    stack = [s[i]]
    while stack:
        i += 1
        if s[i] == '[':
            stack.append('[')
        elif s[i] == ']':
            stack.pop()
    return i


def get_next_num(s, left, right):
    for i in range(left, right):
        if s[i].isdigit():
            return i


def unpack(s, left=0, right=None):
    if right is None:
        right = len(s)
    if left == right:
        return ''
    i = get_next_num(s, left, right)
    if i is None:
        return s[left:right]
    num = int(s[i])
    next_bra_id = get_next_bra_id(s, i + 1)
    left_s = num * unpack(s, i + 2, next_bra_id)
    right_s = unpack(s, next_bra_id + 1, right)
    return s[left:i] + left_s + right_s


def get_max_prefix(res):
    min_s = min(res, key=len)
    max_num = None
    for i, symb in enumerate(min_s):
        is_ok = True
        for el in res:
            if el[i] != symb:
                is_ok = False
                break
        if is_ok:
            max_num = i
        else:
            break
    return max_num


def main():
    n = int(input())
    strs = [unpack(input()) for _ in range(n)]
    max_prefix = get_max_prefix(strs)
    return strs[0][:max_prefix + 1]


if __name__ == '__main__':
    print(main())
