def prepare(t_s):
    h, *m = t_s.split('.')
    if not m:
        m = ['0']
    return int(h), int(m[0])


def main():
    n = int(input())
    times = []
    for _ in range(n):
        start, end = [prepare(s) for s in input().split()]
        times.append((start, end))
    times.sort(key=lambda x: (x[1], x[0]))

    res = []
    for start, end in times:
        if not res:
            res.append((start, end))
            last_end = end
        else:
            if last_end <= start:
                res.append((start, end))
                last_end = end

    print(len(res))
    for line in res:
        for l in line:
            if l[1] != 0:
                print(f'{l[0]}.{l[1]}', end=' ')
            else:
                print(l[0], end=' ')
        print('')


if __name__ == '__main__':
    main()
