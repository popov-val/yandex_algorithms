def main(n, k, s):
    res = []
    find_substr = set()
    l = len(s)
    for i in range(l):
        sub_str = s[i:n + i]
        if sub_str in find_substr:
            break
        else:
            find_substr.add(sub_str)
        cnts = 1
        left = n + i
        right = left + n
        while right <= l:
            sub_str_find = s[left: right]
            if sub_str == sub_str_find:
                cnts += 1
                left = right
                right = left + n
            else:
                left += 1
                right += 1
        if cnts >= k:
            res.append(i)
    return res


if __name__ == '__main__':
    'axniaxaxaxniaxaxaxax'
    # n, k = list(map(int, input().split()))
    # s = input()
    # print(*main(n, k, s))
