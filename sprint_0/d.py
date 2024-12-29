def get_result(n, l, k):
    for i in range(n):
        for j in range(i+1, n):
            sum_ = l[i] + l[j]
            if sum_ == k:
                return l[i],  l[j]
    return [None]


def read_params():
    n = int(input())
    l = list(map(int, input().split()))
    k = int(input())
    return n, l, k


if __name__ == '__main__':
    print(' '.join(map(str, get_result(*read_params()))))
