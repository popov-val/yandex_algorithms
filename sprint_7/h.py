def main():
    n, m = list(map(int, input().split()))
    dp = [[0 for _ in range(m)] for _ in range(n)]
    points = [input() for _ in range(n)][::-1]
    dp[0][0] = int(points[0][0])
    for i in range(1, n):
        dp[i][0] = int(points[i][0]) + int(dp[i - 1][0])

    for i in range(1, m):
        dp[0][i] = int(points[0][i]) + dp[0][i - 1]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = int(points[i][j]) + max(dp[i][j - 1], dp[i - 1][j])

    i, j = n - 1, m - 1
    way = ''
    while i > 0 or j > 0:
        if i == 0:
            way += 'R'
            j -= 1
        elif j == 0:
            way += 'U'
            i -= 1
        elif dp[i][j - 1] > dp[i - 1][j]:
            way += 'R'
            j -= 1
        else:
            way += 'U'
            i -= 1

    return dp[-1][-1], way[::-1]


if __name__ == '__main__':
    m, way = main()
    print(m)
    print(way)
