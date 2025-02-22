if __name__ == '__main__':
    v, e = list(map(int, input().split()))
    vers = [[] for i in range(v)]
    for i in range(e):
        u, v = list(map(int, input().split()))
        vers[u - 1].append(v)
        vers[v - 1].append(u)

    first = int(input())
    stack = [first]
    already = set()
    while stack:
        v = stack.pop()
        if v not in already:
            print(v, end=' ')
            already.add(v)
            els = sorted(vers[v - 1], reverse=True)
            stack.extend(els)
