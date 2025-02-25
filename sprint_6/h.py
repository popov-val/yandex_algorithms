white = 0
gray = 1
black = 2


def get_vers(v, e):
    vers = [[] for _ in range(v)]
    for i in range(e):
        u, v = list(map(int, input().split()))
        vers[u - 1].append(v)
    return vers


if __name__ == '__main__':
    v, e = list(map(int, input().split()))
    vers = get_vers(v, e)
    t_in = [0 for _ in range(v)]
    t_out = [0 for _ in range(v)]
    colors = [0 for _ in range(v)]
    t = 0
    stack = [1]
    while stack:
        cur_v = stack.pop()
        if colors[cur_v-1] == white:
            t_in[cur_v-1] = t
            colors[cur_v-1] = gray
            stack.append(cur_v)
            edges = [ed for ed in vers[cur_v - 1] if colors[ed-1] == white]
            stack.extend(sorted(edges, reverse=True))
            t += 1
        elif colors[cur_v - 1] == gray:
            colors[cur_v - 1] = black
            t_out[cur_v - 1] = t
            t += 1



    for in_, out in zip(t_in, t_out):
        print(in_, out)

