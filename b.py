def sum13(nums):
    s = 0
    if len(nums) > 0 and nums[-1] != 13:
        s = nums[-1]
    for i in range(len(nums)-2, -1, -1):
        if nums[i] != 13 and nums[i + 1] != 13:
            s += nums[i]

    print(s)


sum13([30, 2, 4, 6, 30, 13, 8, 9])
