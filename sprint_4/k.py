max_distant = 20


def add_point(points, x1, y1):
    for _, x, y in points.keys():
        distant = (x - x1) ** 2 + (y - y1) ** 2
        if max_distant ** 2 >= distant:
            points[_, x, y] += 1


if __name__ == '__main__':
    n = int(input())
    points = {}
    for i in range(n):
        x, y = input().split()
        points[i+1, int(x), int(y)] = 0
    p = int(input())

    for _ in range(p):
        x, y = input().split()
        add_point(points, int(x), int(y))

    print()
