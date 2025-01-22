def get_hash_list(a, m, s):
    l = []
    for i in range(len(s) - 1, -1, -1):
        let = s[len(s) - 1 - i]
        l.append(ord(let) * (a ** i) % m)
    return l


def part_hash(a, m, hash_list, left, right):
    pov = right - len(hash_list)
    res = (sum(hash_list[left:right]) / (a ** pov)) % m
    return res


def get_hash(a, m, s):
    h = 0
    for el in s:
        h = (h * a + ord(el)) % m
    return h


if __name__ == '__main__':
    # s = 'abcdef'
    # a = 1000
    # m = 1000009
    a = int(input())
    m = int(input())
    s = input()
    n = int(input())
    for _ in range(n):
        start, end = list(map(int, input().split()))
        hash_end = get_hash(a, m, s[:end])
        hash_start = get_hash(a, m, s[:start-1])
        pov = end - start + 1
        delta = hash_end - hash_start * (a ** pov)
        res = abs(delta) % m
        print(res)
