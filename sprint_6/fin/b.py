from collections import deque


def main():
    cnt = 0
    max_size = 0
    n, m = list(map(int, input().split()))
    shifts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    plate = [input() for _ in range(n)]
    d = deque()
    nums = n * m
    vers = set(range(nums))
    while vers:
        k = vers.pop()
        i = k // m
        j = k % m
        if plate[i][j] == '.':
            continue

        d.append((i, j))
        cnt += 1
        size = 0
        while d:
            i, j = d.popleft()
            size += 1
            for shift_i, shift_j in shifts:
                i_neib, j_neib = i + shift_i, j + shift_j
                if 0 > i_neib or i_neib >= n or 0 > j_neib or j_neib >= m:
                    continue
                neib = i_neib * m + j_neib
                if neib not in vers:
                    continue
                vers.remove(neib)
                if plate[i_neib][j_neib] == '#':
                    d.append((i_neib, j_neib))

        max_size = max(size, max_size)
    return cnt, max_size


if __name__ == '__main__':
    print(*main())
