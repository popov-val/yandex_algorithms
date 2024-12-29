# https://contest.yandex.ru/contest/22450/run-report/129367008/
def func(n, nums):
    d = [0] * n
    d_i = 0
    l_0 = -1
    r_0 = 0
    while l_0 < n - 1:
        if r_0 < n and nums[r_0] != 0:
            r_0 += 1
            continue

        if l_0 < 0:
            d[d_i] = r_0 - d_i
        elif l_0 >= 0 and r_0 < n:
            d[d_i] = min(d_i - l_0, r_0 - d_i)
        else:  # r_0 == n
            d[d_i] = d_i - l_0

        d_i += 1
        if d_i >= r_0:
            l_0 = r_0
            r_0 += 1
    return d


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(' '.join(map(str, func(n, nums))))
