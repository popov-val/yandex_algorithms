from itertools import zip_longest


def func(s, t):
    for a, b in zip_longest(sorted(s), sorted(t)):
        if a != b:
            return b


if __name__ == '__main__':
    s = input()
    t = input()
    print(func(s, t))
