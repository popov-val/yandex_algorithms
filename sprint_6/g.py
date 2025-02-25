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
    dist = [None for _ in range(v_n)]
    d = 0
    dist[first - 1] = d
    while planned:
        cur_v = planned.popleft()
        for v in vers[cur_v - 1]:
            if colors[v - 1] == white:
                colors[v - 1] = gray
                dist[v - 1] = dist[cur_v - 1] + 1
                planned.append(v)
        colors[cur_v - 1] = black
    print(max(dist))
