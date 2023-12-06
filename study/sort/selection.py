from random import randint

nums = [randint(1, 40) for _ in range(20)]

for i in range(len(nums)):
    tmp_min = nums[i]
    tmp_index = i
    for j in range(i+1, len(nums)):
        if tmp_min > nums[j]:
            tmp_index = j
            tmp_min = nums[j]
    nums[tmp_index], nums[i] = nums[i], nums[tmp_index]

print(nums)
