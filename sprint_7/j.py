def main():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    l = max(dp)
    res = []
    c = l
    for i in range(n - 1, -1, -1):
        if dp[i] == c:
            res.append(i + 1)
            c -= 1
    return l, res[::-1]


if __name__ == '__main__':
    l, res = main()
    print(l)
    print(*res)
