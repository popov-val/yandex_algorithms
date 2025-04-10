def main():
    s = input()
    t = input()
    l_s = len(s)
    l_t = len(t)
    prev = list(range(l_s + 1))
    curr = [l_s]
    for i in range(1, l_t + 1):
        curr = [i]
        for j in range(1, l_s + 1):
            if t[i - 1] == s[j - 1]:
                curr.append(prev[j - 1])
            else:
                curr.append(min(curr[j - 1],
                                prev[j], prev[j - 1]) + 1)
        prev = curr

    return curr[-1]


if __name__ == '__main__':
    print(main())
