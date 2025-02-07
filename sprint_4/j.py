def main(a, b):
    min_l, max_l = (a, b) if len(a) <= len(b) else (b, a)
    max_cnt = 0
    for i in range(len(min_l)):
        m = 0
        for j in range(len(max_l)):
            for k in range(1, len(min_l) - i + 1):
                if min_l[i: i + k] == max_l[j:j + k]:
                    m += 1
                else:
                    break
            max_cnt = max(max_cnt, m)
            m = 0
    return max_cnt


if __name__ == '__main__':
    input()
    a = list(map(int, input().split()))
    input()
    b = list(map(int, input().split()))

    print(main(a, b))
