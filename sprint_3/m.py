def get_union_periods(beds):
    prev_left = None
    prev_right = None
    for left, right in sorted(beds, key=lambda x: x[0]):
        if not prev_left and not prev_right:
            prev_left = left
            prev_right = right
            continue

        if prev_right < left:
            yield prev_left, prev_right
            prev_left = left
        prev_right = max(right, prev_right)

    yield prev_left, prev_right


if __name__ == '__main__':
    n = int(input())
    beds = []
    for _ in range(n):
        beds.append(list(map(int, input().split())))

    for l, r in get_union_periods(beds):
        print(l, r)
