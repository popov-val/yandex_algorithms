def bin_search(x, l, left=None, right=None, first=None):
    if left is None:
        left = 0
    if right is None:
        right = len(l)

    if right <= left:
        if first:
            return first, -1
        return -1, -1

    middle = (left + right) // 2

    if x <= l[middle]:
        if first:
            return first, middle
        return bin_search(x * 2, l, middle + 1, right, middle)

    if x > l[middle]:
        return bin_search(x, l, left, middle, first)


if __name__ == '__main__':
    input()
    l = list(map(int, input().split()))
    price = int(input())
    print(*bin_search(price, l))
