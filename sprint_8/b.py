def main():
    s = input()
    t = input()
    delta_len = abs(len(s) - len(t))

    if delta_len == 1:
        s_ord = sum(ord(el) for el in s)
        t_ord = sum(ord(el) for el in t)
        if ord('a') <= abs(s_ord - t_ord) <= ord('z'):
            return 'OK'

    if delta_len == 0:
        cnt_change = sum(s[i] != t[i] for i in range(len(s)))
        if cnt_change <= 1:
            return 'OK'

    return 'FAIL'


if __name__ == '__main__':
    print(main())
