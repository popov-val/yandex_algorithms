# def main_1(sides):
#     n = len(sides)
#     for i in range(n-2):
#         for j in range(i+1, n-1):
#             for k in range(j+1, n):
#                 yield i, j, k

def main(sides):
    sides.sort(reverse=True)
    n = len(sides)
    left = 0
    center = 1
    right = 2
    max_par = 0
    while left < n - 2:

        a, b, c = sides[left], sides[center], sides[right]
        if a < b + c:
            return sum([a, b, c])

        if center == n - 2:
            left += 1
            center = left + 1
            right = center + 1
        elif right == n - 1:
            center += 1
            right = center + 1
        else:
            right += 1
    return max_par


if __name__ == '__main__':
    input()
    sides = list(map(int, input().split()))
    print(main(sides))
