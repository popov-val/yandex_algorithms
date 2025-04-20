# https://contest.yandex.ru/contest/26133/run-report/137056892/
"""
-- ПРИНЦИП РАБОТЫ --
1) Чтение
2) Из "составных" слов собираем бор, струкрута:
word ->
{'w': {'o': {'r': {'d': 'is_end': True}}}}
3) Собираем dp, каждый элемент - можно ли разбить строку длины i
    - Пустая строка - True
    - Проходимся по каждому элементу dp
    - Если dp[i] = False проходим дальше
    - Проходимся по каждому символу от i до n
    - Ищем по бору символ и если нет прекращаем
    - Если есть, проверяем конец ли это


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Так как проходимся по каждому символу для dp и ищем по каждому "составному" символу

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
M - длина слова
N - кол-во слов
L - длина строки
O(M*L)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(M*N) - бор
O(L) - dp
Итого: O(M*N) + O(L)
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
