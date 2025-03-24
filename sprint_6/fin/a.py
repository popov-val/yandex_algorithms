# https://contest.yandex.ru/contest/25070/run-report/135437324/
def get_edges(e):
    edges = []
    for _ in range(e):
        u, v, l = list(map(int, input().split()))
        edges.append((u, v, l))
    edges.sort(key=lambda x: x[2])
    return edges


def recolor(ver, color, colors, mst):
    for_recolor = [ver]
    while for_recolor:
        f_r = for_recolor.pop()
        if colors[f_r] != color:
            colors[f_r] = color
            for_recolor.extend(mst[f_r])


def main():
    n, m = list(map(int, input().split()))
    all_edges = get_edges(m)
    colors = [0 for _ in range(n + 1)]
    mst = [[] for _ in range(n + 1)]
    weight = 0
    max_color = 1
    while all_edges:
        add_mst_flag = False
        u, v, l = all_edges.pop()
        if u == v:
            continue
        if not colors[u] and not colors[v]:
            colors[u] = max_color
            colors[v] = max_color
            max_color += 1
            add_mst_flag = True
        elif not colors[u]:
            colors[u] = colors[v]
            add_mst_flag = True
        elif not colors[v]:
            colors[v] = colors[u]
            add_mst_flag = True
        elif colors[v] != colors[u]:
            add_mst_flag = True
            if colors[v] < colors[u]:
                recolor_ver = u
                color = colors[v]
            else:
                recolor_ver = v
                color = colors[u]
            recolor(recolor_ver, color, colors, mst)

        if add_mst_flag:
            weight += l
            mst[u].append(v)
            mst[v].append(u)

    if not all(colors[1:]) and n > 1:
        return 'Oops! I did it again'
    return weight


if __name__ == '__main__':
    print(main())
