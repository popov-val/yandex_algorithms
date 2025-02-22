if __name__ == '__main__':
    v, e = list(map(int, input().split()))
    vers = [[0 for j in range(v)] for i in range(v)]
    for i in range(e):
        u, v = list(map(int, input().split()))
        vers[u - 1][v - 1] = 1

    for el in vers:
        print(*el)



