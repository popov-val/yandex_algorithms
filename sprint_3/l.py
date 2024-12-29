def bin_search(x, l, left=None):
    if left is None:
        left = 0
    right = len(l) - 1
    index = None
    middle = -1
    while middle != (left + right) // 2:
        middle = (left + right) // 2

        if x <= l[middle]:
            index = middle
            right = middle
        else:
            left = middle + 1

    return index


if __name__ == '__main__':
    input()
    l = list(map(int, input().split()))
    price = int(input())
    first = bin_search(price, l)

    if first is not None:
        second = bin_search(price * 2, l, first)
    else:
        second = None
    print(str(-1 if first is None else first + 1), end=' ')
    print(str(-1 if second is None else second + 1))
