def main(n, k):
    if n < 2:
        return 1
    prev_1 = 2
    prev_2 = 1
    for _ in range(n - 2):
        accum = (prev_1 + prev_2) % 10**k
        prev_2 = prev_1
        prev_1 = accum
    return accum


if __name__ == '__main__':
    n, k = [int(l) for l in input().split()]
    print(main(n, k))
