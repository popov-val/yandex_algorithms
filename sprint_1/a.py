def func(a, x, b, c):
    return a * x * x + b * x + c


if __name__ == '__main__':
    a, x, b, c = map(int, input().split())
    print(func(a, x, b, c))