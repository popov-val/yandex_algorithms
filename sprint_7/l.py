def main():
    n, m = list(map(int, input().split()))
    dp = None
    w = list(map(int, input().split()))
    for el in w:
        if not dp:
            dp = [el if el <= j else 0 for j in range(m + 1)]
            continue
        els = []
        for j in range(m + 1):
            curr = el if el <= j else 0
            rest = j - el
            if rest >= 0:
                curr += dp[rest]
            els.append(max(dp[j], curr))
        dp = els
    return dp[-1]


if __name__ == '__main__':
    print(main())
