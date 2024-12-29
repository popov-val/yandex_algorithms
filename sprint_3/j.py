def bubble_sort(n, l):
    not_sort = True
    for j in range(n-1, 0, -1):
        sort_flag = False
        for i in range(j):
            if l[i] > l[i + 1]:
                sort_flag = True
                not_sort = False
                l[i], l[i + 1] = l[i + 1], l[i]

        if sort_flag or not_sort:
            print(*l)
        if not sort_flag:
            break


if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    bubble_sort(n, l)
