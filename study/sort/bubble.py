from random import randint

nums = [randint(1, 40) for _ in range(20)]

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print(nums)
