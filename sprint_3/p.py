def main(nums):
    for i in range(len(nums)):
        nums[i] = nums[i], i
    nums.sort(key=lambda x: x[0])
    print(1)


if __name__ == '__main__':
    nums = [3, 2, 0, 1, 4, 6, 5]
    main(nums)
