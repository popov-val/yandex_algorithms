def get_res():
    n = int(input())
    a = input().split()
    b = input().split()
    for i in range(n):
        a.insert(i * 2 + 1, b[i])

    print(' '.join(a))


if __name__ == '__main__':
    get_res()