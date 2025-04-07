def main():
    n, k = list(map(int, input().split()))
    dp = [0]
    for i in range(1, n):
        start = max(0, i - k)
        shift = 1 if k >= i else 0
        dp.append(sum(dp[start:i], shift))

    return dp[-1] % (10 ** 9 + 7)


if __name__ == '__main__':
    print(main())
