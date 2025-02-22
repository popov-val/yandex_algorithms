if __name__ == '__main__':
    v, e = list(map(int, input().split()))
    vers = [[] for i in range(v)]
    for i in range(e):
        u, v = list(map(int, input().split()))
        vers[u - 1].append(v)

    for el in vers:
        print(len(el), *el)
