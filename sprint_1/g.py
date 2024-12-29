def func(n):
    i = 2
    nums = []
    while i * i <= n:
        if n % i == 0:
            nums.append(i)
            n = n / i
            i = 2
        else:
            i += 1
    nums.append(int(n))
    return nums


if __name__ == '__main__':
    n = int(input())
    print(' '.join(map(str, func(n))))
