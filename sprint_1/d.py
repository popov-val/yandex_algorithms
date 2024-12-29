def func(n, l):
    if n == 1:
        return 1
    cnt = l[0] > l[1]
    cnt += l[n-1] > l[n-2]
    for i in range(1, n - 1):
        cnt += l[i - 1] < l[i] > l[i + 1]
    return cnt


if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    print(func(n, l))
