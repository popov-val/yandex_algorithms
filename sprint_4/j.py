def main(a):
    # res = {el: [] for el in a}
    res = {}
    next_ = []
    for el in a:
        if not res:
            res[el] = next_
        else:
            new_next = []
            next_.append({el: new_next})
            next_ = new_next
            if res.get(el):
                pass
            else:
                res[el] = next_

    return res


if __name__ == '__main__':
    # input()
    # a = list(map(int, input().split()))
    # input()
    # b = list(map(int, input().split()))

    a = [1, 1, 2, 3]

    print(main(a))

a = [1, 2, 3]
stuct = {
    1: [{2: [{3: []}]}, {1: [{2: [{3: []}]}]}],
    2: [{3: []}],
    3: []
}
