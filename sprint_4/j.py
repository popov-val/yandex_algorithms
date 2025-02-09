def get_structure(a):
    d = {}
    for i, el in enumerate(a):
        if d.get(el):
            d[el].add(i)
        else:
            d[el] = {i}
    return d


def get_inc_in_set(prev, s):
    for el in prev:
        if el + 1 in s:
            return el + 1
    # return False


def main(a, b):
    d = get_structure(a)
    prev = None
    max_cnt = 0
    cnt = 0
    for el in b:
        s = d.get(el)
        if not s:
            max_cnt = max(max_cnt, cnt)
            prev = None
            cnt = 0
            continue
        if not prev:
            prev = s
            cnt += 1
            continue

        el = get_inc_in_set(prev, s)
        if el:
            prev = {el}
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            prev = s
            cnt = 1
    return max(max_cnt, cnt)


if __name__ == '__main__':
    input()
    a = list(map(int, input().split()))
    input()
    b = list(map(int, input().split()))

    print(main(a, b))
