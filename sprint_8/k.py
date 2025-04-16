def main():
    a = input()
    b = input()
    cnt_a = ''.join(el for el in a if ord(el) % 2 == 0)
    cnt_b = ''.join(el for el in b if ord(el) % 2 == 0)
    if cnt_a < cnt_b:
        res = -1
    elif cnt_a == cnt_b:
        res = 0
    else:
        res = 1
    return res


if __name__ == '__main__':
    print(main())
