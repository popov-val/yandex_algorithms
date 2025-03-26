from collections import deque


def get_number_plate(n):
    empty_row = None
    yield empty_row
    for i in range(n):
        yield input()
    yield empty_row


def add_to_graph(plate, graph, m, num_row):
    for i in range(m):
        if plate[1][i] == '.':
            continue
        graph[(num_row, i)] = []
        for shift in range(-1, 2, 2):
            if 0 <= i + shift < m and plate[1][i + shift] != '.':
                graph[(num_row, i)].append((num_row, i + shift))
            if plate[1 + shift] and plate[1 + shift][i] != '.':
                graph[(num_row, i)].append((num_row + shift, i))


def get_graph():
    n, m = list(map(int, input().split()))
    plate = deque()
    graph = {}
    next_plate = get_number_plate(n)
    plate.append(next(next_plate))
    plate.append(next(next_plate))
    num_row = 0
    while num_row != n:
        num_row += 1
        plate.append(next(next_plate))
        add_to_graph(plate, graph, m, num_row)
        plate.popleft()

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
            if u in visited:
                continue
            visited.add(u)
            cnt += 1
            for_color.extend(graph[u])
        max_cnt = max(cnt, max_cnt)

    return max_color, max_cnt


def main():
    graph = get_graph()
    metrics = get_metrics(graph)
    print(*metrics)


if __name__ == '__main__':
    main()
