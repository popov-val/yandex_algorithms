def main(n, k, houses):
    cnt = 0
    for house in sorted(houses):
        if house <= k:
            cnt += 1
            k -= house
        if cnt == n or house > k:
            return cnt
    return cnt



if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    houses = list(map(int, input().split()))

    print(main(n, k, houses))
