def func(num):
    while num != 1:
        if num % 4 == 0:
            num = num / 4
        else:
            return False
    return True


if __name__ == '__main__':
    num = int(input())
    print(func(num))
