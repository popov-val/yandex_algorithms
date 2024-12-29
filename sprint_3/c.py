def main(s, t):
    i = 0
    for t_el in t:
        if t_el == s[i]:
            i += 1
        if len(s) == i:
            return True

    return False  # len(s) == i


if __name__ == '__main__':
    s = input()
    t = input()
    print(main(s, t))
