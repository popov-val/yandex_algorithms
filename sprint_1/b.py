def func(a, b, c):
    if a % 2 == b % 2 == c % 2:
        return 'WIN'
    return 'FAIL'


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(func(a, b, c))
