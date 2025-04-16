def main():
    n = int(input())
    x = list(map(int, input().split()))
    m = int(input())
    a = list(map(int, input().split()))
    res = []
    for i in range(n - (m - 1)):
        c = None
        for j in range(m):
            diff = x[i + j] - a[j]
            if c is None:
                c = diff
                continue
            if c != diff:
                c = None
                break
        if c is not None:
            res.append(i + 1)
    return res


if __name__ == '__main__':
    print(*main())
