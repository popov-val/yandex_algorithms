from collections import deque


def main():
    cnt = 0
    max_size = 0
    n, m = list(map(int, input().split()))
    shifts = [1, -1, m, -m]
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

        d.append(k)
        cnt += 1
        size = 0
        while d:
            num = d.popleft()
            size += 1
            for shift in shifts:
                neib = num + shift
                if neib < 0 or neib >= nums:
                    continue
                if shift in [-1, 1] and neib // m != num // m:
                    continue
                if neib not in vers:
                    continue
                vers.remove(neib)
                if plate[neib // m][neib % m] == '#':
                    d.append(neib)

        max_size = max(size, max_size)
    return cnt, max_size


if __name__ == '__main__':
    print(*main())
