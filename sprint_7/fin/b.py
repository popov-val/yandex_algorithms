# https://contest.yandex.ru/contest/25597/run-report/136734496/
"""
-- ПРИНЦИП РАБОТЫ --
Если все числа должны разбиваться на 2 суммы, значит
Далее сводим задачу к "рюкзаку", только вместимость будет половина от суммы
После нахождения первых подходящий чисел
 - считаем их сумму (там будут и лишние числа),
 - вычитаем из этого половину (получив сумму оставшихся)
 - добавляем оставшийся "хвост"
Если эта сумма равна полусумме, значит эти числа можно разбить

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Задача сводится к "задаче о рюкзаке"
Походя каждый элемент и добавяя его к dp, считаем сумму, которую можно получить
Таким образом, получаем сумму первых чисел
Остальные можно считать обычным суммированием

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
N - кол-во чисел
M - размер "рюкзака"
Итого: O(N*M)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Итого: O(M*2) - два массива длиной в размер "рюкзака"
"""


def main():
    input()
    nums = list(map(int, input().split()))
    s = sum(nums)
    if s % 2 != 0:
        return False
    half = s // 2
    prev = [0] * (half + 1)
    curr = [0] * (half + 1)
    for i, num in enumerate(nums, start=1):
        for size in range(half + 1):
            value = num if num <= size else 0
            rest = size - value
            if rest > 0:
                value += prev[rest]
            curr[size] = value if value >= prev[size] else prev[size]
        if curr[-1] == half:
            check = sum(nums[:i]) - half + sum(nums[i:])
            return check == half
        prev = curr
        curr = [0] * (half + 1)
    return False


if __name__ == '__main__':
    print(main())
