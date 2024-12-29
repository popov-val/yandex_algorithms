def func(n, m, mat, x, y):
    neib = []
    for i in range(-1, 2, 2):
        if 0 <= x + i < m:
            neib.append(mat[y][x + i])

    for i in range(-1, 2, 2):
        if 0 <= y + i < n:
            neib.append(mat[y + i][x])
    neib.sort()
    return neib


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    y = int(input())
    x = int(input())

    print(' '.join(map(str, func(n, m, mat, x, y))))
