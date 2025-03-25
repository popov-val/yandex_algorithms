from collections import deque
from line_profiler import profile


@profile
def get_number_plate(f, n, graph):
    empty_row = None
    yield empty_row
    vers_cnt = 0
    for i in range(n):
        row = []
        for s in f.readline():
            if s == '#':
                vers_cnt += 1
                row.append(vers_cnt)
                graph.append([])
            else:
                row.append(s)
        yield row
    yield None


@profile
def add_to_graph(plate, graph, m):
    for i in range(m):
        point = plate[1][i]
        if point == '.':
            continue

        for shift in range(-1, 2, 2):
            if 0 <= i + shift < m and plate[1][i + shift] != '.':
                graph[point].append(plate[1][i + shift])
            if plate[1 + shift] and plate[1 + shift][i] != '.':
                graph[point].append(plate[1 + shift][i])


@profile
def get_graph(f):
    n, m = list(map(int, f.readline().split()))
    plate = deque()
    graph = [None]
    next_plate = get_number_plate(f, n, graph)
    plate.append(next(next_plate))
    plate.append(next(next_plate))
    i = n
    while i:
        i -= 1
        plate.append(next(next_plate))
        add_to_graph(plate, graph, m)
        plate.popleft()

    return graph


@profile
def get_metrics(graph):
    visited = [False for _ in range(len(graph))]
    max_color = 0
    max_cnt = 0
    for v in range(1, len(graph)):
        if visited[v]:
            continue
        cnt = 0
        max_color += 1
        for_color = [v]
        while for_color:
            u = for_color.pop()
            if visited[u]:
                continue
            visited[u] = True
            cnt += 1
            for_color.extend(graph[u])
        max_cnt = max(cnt, max_cnt)

    return max_color, max_cnt


@profile
def main():
    with open('data/input.txt') as f:
        graph = get_graph(f)
    metrics = get_metrics(graph)
    print(*metrics)


if __name__ == '__main__':
    main()
