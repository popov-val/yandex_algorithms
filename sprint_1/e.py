def func(n, s):
    max_s = ''
    for sub_s in s.split():
        if len(max_s) < len(sub_s):
            max_s = sub_s
    return max_s


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(func(n, s))
    print(len(func(n, s)))
