def merge(arr, lf, mid, rg):
    l = lf
    r = mid
    res = []
    while l < mid and r < rg:
        left = arr[l]
        right = arr[r]
        if left <= right:
            res.append(arr[l])
            l += 1
        else:
            res.append(arr[r])
            r += 1

    if l < mid:
        res.extend(arr[l:mid])
    else:
        res.extend(arr[r:rg])
    return res


def merge_sort(arr, lf, rg):
    mid = (rg + lf) // 2
    if mid - lf > 1:
        merge_sort(arr, lf, mid)
    if rg - mid > 1:
        merge_sort(arr, mid, rg)

    res = merge(arr, lf, mid, rg)
    arr[lf: rg] = res


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
