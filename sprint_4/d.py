def main(a, m, s):
    h = 0
    for el in s:
        h = (h * a + ord(el)) % m
    return h


if __name__ == '__main__':
    a = int(input())
    m = int(input())
    s = input()

    print(main(a, m, s))
