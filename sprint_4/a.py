if __name__ == '__main__':
    n = int(input())
    s = {}
    for _ in range(n):
        s[input()] = None

    for el in s:
        print(el)
