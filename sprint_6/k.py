from collections import deque


def get_vers(v, e):
    vers = [[] for _ in range(v)]
    for i in range(e):
        u, v, l = list(map(int, input().split()))
        vers[u - 1].append((v - 1, l))
        vers[v - 1].append((u - 1, l))
    for v in vers:
        v.sort(key=lambda x: x[1])
    return vers


def get_dist(vers, s, n):
    vis = [False for _ in range(n)]
    dist = [-1 for _ in range(n)]
    dist[s] = 0
    queue = deque()
    queue.append(s)
    while queue:
        v = queue.popleft()
        if vis[v]:
            continue
        vis[v] = True

        neighbours = vers[v]
        for neig, n_l in neighbours:
            if dist[neig] == -1 or dist[neig] > dist[v] + n_l:
                dist[neig] = dist[v] + n_l

        first = True
        for v, _ in neighbours:
            if not vis[v]:
                if first:
                    queue.appendleft(v)
                    first = False
                else:
                    queue.append(v)

    return dist


def main():
    n, m = list(map(int, input().split()))
    vers = get_vers(n, m)
    res = []
    for v in range(len(vers)):
        res.append(get_dist(vers, v, n))
    for i in range(n):
        for j in range(n):
            if i > j:
                m = min(res[i][j], res[j][i])
                res[i][j] = m
                res[j][i] = m
    for r in res:
        print(*r)


if __name__ == '__main__':
    main()
