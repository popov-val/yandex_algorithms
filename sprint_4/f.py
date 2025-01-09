def get_hash(a, m, s):
    h = 0
    for el in s:
        h = (h * a + ord(el)) % m
    return h


def part_hash():
    pass


if __name__ == '__main__':
    a = int(input())
    m = int(input())
    s = input()
    main_hash = get_hash(a, m, s)
    n = int(input())
    for _ in range(n):
        start, end = list(map(int, input().split()))
        print(part_hash(a, m, s))
