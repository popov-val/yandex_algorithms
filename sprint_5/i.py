import math


def get_cnt(n):
    f_n = math.factorial(n)
    return int(math.factorial(n * 2) / (f_n * f_n * (n + 1)))


if __name__ == '__main__':
    print(get_cnt(int(input())))
