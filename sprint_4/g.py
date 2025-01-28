def main(n, s, nums):
    history = set()
    result = set()
    nums.sort()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                a = s - nums[i] - nums[j] - nums[k]
                if a in history:
                    result.add((a, nums[i], nums[j], nums[k]))
        history.add(nums[i])
    return result


if __name__ == '__main__':
    n = int(input())
    s = int(input())
    nums = list(map(int, input().split()))
    res = main(n, s, nums)
    print(len(res))
    for el in sorted(res):
        print(*el)
