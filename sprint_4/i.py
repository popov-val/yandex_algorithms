def main(list_str):
    list_set = [(i, sorted(s)) for i, s in enumerate(list_str)]
    list_set.sort(key=lambda x: (x[1], x[0]))
    prev_i, prev_s = None, None
    res = []
    for i, s in list_set:
        if not prev_s:
            prev_i, prev_s = i, s
            res_i = [i]
            continue

        if prev_s == s:
            res_i.append(i)
        else:
            res.append(res_i)
            res_i = [i]
            prev_i, prev_s = i, s
    res.append(res_i)
    return res


if __name__ == '__main__':
    input()
    for nums in sorted(main(input().split())):
        print(*nums)
