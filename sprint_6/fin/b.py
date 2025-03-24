def get_plate():
    n, _ = list(map(int, input().split()))
    return [input() for _ in range(n)]


def process_neighbours(graph, plate, i, j, n, m):
    for shift in range(-1, 2, 2):
        if 0 <= j + shift < m and plate[i][j + shift] == '#':
            graph[(i, j)].append((i, j + shift))
        if 0 <= i + shift < n and plate[i + shift][j] == '#':
            graph[(i, j)].append((i + shift, j))


def get_graph(plate):
    graph = {}
    n = len(plate)
    for i in range(n):
        m = len(plate[i])
        for j in range(m):
            if plate[i][j] == '#':
                graph[(i, j)] = []
                process_neighbours(graph, plate, i, j, n, m)

    return graph


def get_metrics(graph):
    visited = set()
    max_color = 0
    max_cnt = 0
    for v in graph.keys():
        if v in visited:
            continue
        cnt = 0
        max_color += 1
        for_color = [v]
        while for_color:
            u = for_color.pop()
            if u not in visited:
                visited.add(u)
                cnt += 1
                for_color.extend(graph[u])
        max_cnt = max(cnt, max_cnt)

    return max_color, max_cnt


def main():
    plate = get_plate()
    graph = get_graph(plate)
    metrics = get_metrics(graph)
    print(*metrics)


if __name__ == '__main__':
    main()
