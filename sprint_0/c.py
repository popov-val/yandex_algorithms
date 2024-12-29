def get_result(n, l, k):
    sum_k = sum(l[:k])
    res_sum = [sum_k / k]
    for i in range(n - k):
        sum_k -= l[i]
        sum_k += l[i + k]
        res_sum.append(sum_k / k)
    return res_sum


def read_params():
    n = int(input())
    l = list(map(int, input().split()))
    k = int(input())
    return n, l, k


if __name__ == '__main__':
    n, l, k = read_params()
    print(' '.join(map(str, get_result(n, l, k))))
