# https://contest.yandex.ru/contest/25070/run-report/135437324/
"""
-- ПРИНЦИП РАБОТЫ --
Вдохновлено алгоритмом Краскала
1) Читаем все ребра и записываем в массив (get_edges)
2) Сортируем по возрастанию веса ребра (get_edges)
3) Проходимся по всем ребрам, каждый раз берем с конца листа (от самого большого)
4) Для каждого ребра:
    1) Проверяем что вершины разные
    2) Если обе вершины не покращены, красим и добавляем к MST
    3) Если одина из вершин не покрашена красим в цвет другой и добавляем к MST
    4) Если обе покрашены, перекрашиваем ту у которой номер цвета больше
5) Проверяем, что все вершины покрашены в один цвет и из кол-во больше 1

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Так как мы проходимся по всем ребрам графа все значимые вершины будут посещены/покрашены
Процесс перекраски позваляет учесть объединяемые "подграфы" в один

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
N - кол-во вершин
M - кол-во ребер
O(MlogM) - на чтение и сортировку
O(M) - проход каждого ребра
    O(C) - Для одной из вершин ребра возможно перекраска и перекраска его соседей,
            где С кол-во перекрашиваемых вершин (худший случай N)
Итого: O(MlogM) + O(M*N)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(M) - на сами ребра
O(N) - на сохранение цвета вершин
O(N*M*2) - на сохранение MST (на 2 так как граф неориентированный)
O(C) - на очередь вершин для перекраски
Итого: O(M) + O(N) + O(N*M*2) + O(C)
"""


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
