def func(a, b):
    sum_ = ''
    max_len = max(len(a), len(b))
    next_rank = 0
    for i in range(max_len):
        val_a = int(a[-i - 1]) if i < len(a) else 0
        val_b = int(b[-i - 1]) if i < len(b) else 0

        digit = val_a + val_b + next_rank
        sum_ += str(digit % 2)
        next_rank = digit // 2

    if next_rank > 0:
        sum_ += str(next_rank % 2)

    return sum_[::-1]


if __name__ == '__main__':
    a = input()
    b = input()
    print(func(a, b))
