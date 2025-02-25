from collections import deque

white = 0
gray = 1
black = 2

if __name__ == '__main__':
    v_n, e = list(map(int, input().split()))
    vers = [[] for i in range(v_n)]
    for i in range(e):
        u, v = list(map(int, input().split()))
        vers[u - 1].append(v)
        vers[v - 1].append(u)

    first = int(input())
    planned = deque()
    planned.append(first)
    colors = [white for _ in range(v_n)]
    while planned:
        cur_v = planned.popleft()
        if colors[cur_v - 1] == white:
            colors[cur_v - 1] = gray
            print(cur_v, end=' ')
            els = sorted(vers[cur_v - 1])
            planned.extend([cur_v] + els)
        elif colors[cur_v - 1] == gray:
            colors[cur_v - 1] = black
