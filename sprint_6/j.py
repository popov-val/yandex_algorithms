white = 0
gray = 1
black = 2


def get_vers(v, e):
    vers = [[] for _ in range(v)]
    for i in range(e):
        u, v = list(map(int, input().split()))
        vers[v - 1].append(u)
    return vers


if __name__ == '__main__':
    v, e = list(map(int, input().split()))
    vers = get_vers(v, e)
    colors = [0 for _ in range(v)]
    order = []
    gen = (i + 1 for i, el in enumerate(colors) if el == white)
    for v in gen:
        stack = [v]
        node_order = []
        while stack:
            cur_v = stack.pop()
            if colors[cur_v - 1] == white:
                colors[cur_v - 1] = gray
                stack.append(cur_v)
                edges = [ed for ed in vers[cur_v - 1] if colors[ed - 1] == white]
                stack.extend(sorted(edges, reverse=False))
            elif colors[cur_v - 1] == gray:
                colors[cur_v - 1] = black
                node_order.append(cur_v)
        order.extend(node_order)

    print(*order)
