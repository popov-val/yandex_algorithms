def get_result(n, l, k):
    for i in range(n):
        par = k - l[i]
        if par in l[i+1:]:
            return l[i], par

    return [None]


def read_params():
    n = int(input())
    l = list(map(int, input().split()))
    k = int(input())
    return n, l, k


if __name__ == '__main__':
    print(' '.join(map(str, get_result(*read_params()))))
