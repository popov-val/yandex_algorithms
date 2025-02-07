max_distant = 400


def add_point(points, x1, y1):
    for n, x, y in points.keys():
        distant = (x - x1) ** 2 + (y - y1) ** 2
        if distant <= max_distant:
            points[n, x, y][1] += 1


if __name__ == '__main__':
    n = int(input())
    points = {}
    for i in range(n):
        x, y = input().split()
        points[i, int(x), int(y)] = [i, 0]
    p = int(input())

    for _ in range(p):
        x, y = input().split()
        add_point(points, int(x), int(y))

    print(max(points.values(), key=lambda x: (x[1], -x[0]))[0] + 1)
