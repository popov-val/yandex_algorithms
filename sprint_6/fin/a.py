# https://contest.yandex.ru/contest/25070/run-report/135817716/
"""
-- ПРИНЦИП РАБОТЫ --
Вдохновлено алгоритмом Краскала
Источник: https://neerc.ifmo.ru/wiki/index.php?title=%D0%A1%D0%9D%D0%9C_(%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B8_%D1%81_%D0%B2%D0%B5%D1%81%D0%BE%D0%B2%D0%BE%D0%B9_%D1%8D%D0%B2%D1%80%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%BE%D0%B9)
1) Читаем все ребра и записываем в массив (get_edges)
2) Сортируем по возрастанию веса ребра (get_edges)
3) Проходимся по всем ребрам, каждый раз берем с конца листа (от самого большого)
4) Для каждого ребра:
    1) Проверяем что вершины разные
    2) Если обе вершины не покращены, красим и добавляем к MST
    3) Если одина из вершин не покрашена красим в цвет другой и добавляем к MST
    4) Если обе покрашены, перекрашиваем ту у которой количество вершин меньше
5) Проверяем, что все вершины покрашены в один цвет и из кол-во больше 1

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Так как мы проходимся по всем ребрам графа все значимые вершины будут посещены/покрашены
Процесс перекраски позваляет учесть объединяемые "подграфы" в один

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
N - кол-во вершин
M - кол-во ребер
O(MlogM) - на чтение и сортировку
O(M) - проход каждого ребра
    O(ClogC) - Для одной из вершин ребра возможно перекраска и перекраска его соседей,
            где С кол-во перекрашиваемых вершин
Итого: O(MlogM) + O(M*ClogC)
P.S. Только почему-то тесты стали дольше работать

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(M) - на сами ребра
O(N) - на сохранение цвета вершин
O(N) - на сохранение кол-ва вершин разных цветов
O(N*(N-1)*2) - на сохранение MST (на 2 так как граф неориентированный)
O(C) - на очередь вершин для перекраски
Итого: O(M) + O(N) + O(N) + O(N*M*2) + O(C)
"""


def get_edges(e):
    edges = []
    for _ in range(e):
        u, v, l = list(map(int, input().split()))
        edges.append((u, v, l))
    edges.sort(key=lambda x: x[2])
    return edges


def recolor(ver, new_color, old_color, colors, mst, colors_cnts):
    for_recolor = [ver]
    while for_recolor:
        f_r = for_recolor.pop()
        if colors[f_r] != new_color:
            colors[f_r] = new_color
            for_recolor.extend(mst[f_r])
    colors_cnts[new_color] += colors_cnts[old_color]
    colors_cnts.pop(old_color)


def main():
    n, m = list(map(int, input().split()))
    all_edges = get_edges(m)
    colors = [0 for _ in range(n + 1)]
    colors_cnts = {1: 0}
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
            colors_cnts[max_color] += 2
            max_color += 1
            colors_cnts[max_color] = 0
            add_mst_flag = True
        elif not colors[u]:
            colors[u] = colors[v]
            colors_cnts[max_color] += 1
            add_mst_flag = True
        elif not colors[v]:
            colors[v] = colors[u]
            colors_cnts[max_color] += 1
            add_mst_flag = True
        elif colors[v] != colors[u]:
            add_mst_flag = True
            if colors_cnts[colors[v]] < colors_cnts[colors[u]]:
                recolor_ver = u
                new_color = colors[v]
                old_color = colors[u]
            else:
                recolor_ver = v
                new_color = colors[u]
                old_color = colors[v]
            recolor(recolor_ver, new_color, old_color, colors, mst, colors_cnts)

        if add_mst_flag:
            weight += l
            mst[u].append(v)
            mst[v].append(u)

    if not all(colors[1:]) and n > 1:
        return 'Oops! I did it again'
    return weight


if __name__ == '__main__':
    print(main())
