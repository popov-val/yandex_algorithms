def main():
    l = input()
    dp = [0] * len(l)
    for i in range(1, len(l)):
        prev = dp[i - 1]
        postfix = l[i]
        while prev > 0 and postfix != l[prev]:
            prev = dp[prev - 1]

        if postfix == l[prev]:
            dp[i] = prev + 1
    return dp


if __name__ == '__main__':
    print(*main())
