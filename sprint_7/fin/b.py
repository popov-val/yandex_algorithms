def main():
    n = 4 #int(input())
    nums = list(map(int, '1 5 7 1'.split()))
    s = sum(nums)
    if s % 2 != 0:
        return False
    half = (s // 2)
    cnt = 0
    dp = [[tuple() for _ in range(half+1)] for _ in range(n+1)]
    for i, num in enumerate(nums, start=1):
        for size in range(half+1):
            els = [num] if num <= size else []
            rest = size - sum(els)
            if rest > 0:
                els += dp[i-1][rest]
            dp[i][size] = tuple(sorted(els)) if sum(els) >= sum(dp[i-1][size]) else dp[i-1][size]
        if sum(dp[i][-1]) == half:
            cnt += 1
    return cnt == 2


if __name__ == '__main__':
    print(main())
