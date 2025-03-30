def main():
    n = int(input())
    l = list(map(int, input().split()))
    i = 0
    cost = 0
    on_hand = None
    while i < n - 1:
        if on_hand is None:
            if l[i] < l[i + 1]:
                on_hand = l[i]
        else:
            if l[i] >= l[i + 1]:
                cost += l[i] - on_hand
                on_hand = None
        i += 1
    if l[i - 1] < l[i] and on_hand:
        cost += l[i] - on_hand
    return cost


if __name__ == '__main__':
    print(main())
