def main(s):
    cnts = {'0': 0, '1': 0}
    for el in s:
        cnts[el] += 1

    left = 0
    right = len(s) - 1
    while left < right:
        if cnts['0'] == cnts['1']:
            return right - left + 1

        if cnts[s[left]] > cnts[s[right]]:
            cnts[s[left]] -= 1
            left += 1
            continue
        if cnts[s[left]] < cnts[s[right]]:
            cnts[s[right]] -= 1
            right -= 1
            continue
        if cnts[s[left]] == cnts[s[right]]:
            pass

    return 0


if __name__ == '__main__':
    # input()
    # s = input().split()

    # s = '1 0 0 1 0 0 0 1'.split()
    s = '0 0 1 0 1 1 1 0 0 0'.split()
    print(main(s))
