def main(l):
    cnts = [0] * 3
    for el in l:
        cnts[el] += 1
    i = 0
    for el, cnt in enumerate(cnts):
        for _ in range(cnt):
            l[i] = el
            i += 1
    return l


if __name__ == '__main__':
    input()
    l = list(map(int, input().split()))
    print(*main(l))
