# https://contest.yandex.ru/contest/26133/run-report/137056892/
"""
-- ПРИНЦИП РАБОТЫ --
1)

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


def add(s, symb):
    for el in s:
        symb[el] = symb.get(el, {})
        symb = symb[el]
    symb['is_end'] = True


def main():
    t = input().strip()
    t_len = len(t)
    n = int(input())
    symbol = {}
    for _ in range(n):
        add(input(), symbol)

    dp = [False] * (t_len + 1)
    dp[0] = True

    for i in range(t_len + 1):
        if not dp[i]:
            continue

        curr_symb = symbol
        for j in range(i, t_len):
            curr_symb = curr_symb.get(t[j])
            if not curr_symb:
                break
            if curr_symb.get('is_end'):
                dp[j + 1] = True

    return 'YES' if dp[-1] else 'NO'


if __name__ == '__main__':
    print(main())
