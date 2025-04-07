from collections import deque
from line_profiler import profile


@profile
def main(f):
    n, m = list(map(int, f.readline().split()))
    dp = deque(maxlen=2)
    w = list(map(int, f.readline().split()))
    w.append(m)
    w.sort()
    for el in w[0:n]:
        if not dp:
            dp.append([el for _ in range(n+1)])
            continue
        els = []
        for i, size in enumerate(w):
            curr = el if el <= size else 0
            rest = size - el

            if rest > 0:
                for j in range(i - 1, -1, -1):
                    if curr + dp[-1][j] <= size:
                        curr += dp[-1][j]
                        break
            els.append(max(dp[-1][i], curr))
        dp.append(els)
    return dp[-1][-1]


if __name__ == '__main__':
    with open('data/input_1.txt') as f:
        print(main(f))
