def main(n):
    if n in [0, 1]:
        return 1
    return main(n - 1) + main(n - 2)


if __name__ == '__main__':
    print(main(int(input())))
