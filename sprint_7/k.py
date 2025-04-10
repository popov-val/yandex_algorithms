def main():
    n = int(input())
    a = input().split()
    m = int(input())
    b = input().split()
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    a_id = []
    b_id = []
    i, j = n, m
    while dp[i][j] != 0:
        if a[i - 1] == b[j - 1]:
            a_id.append(i)
            b_id.append(j)
            i -= 1
            j -= 1
            continue
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1
    return dp[-1][-1], a_id[::-1], b_id[::-1]


if __name__ == '__main__':
    m, a_l, b_l = main()
    print(m)
    print(*a_l)
    print(*b_l)
