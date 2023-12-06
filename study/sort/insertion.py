from random import randint

nums = [randint(1, 40) for _ in range(20)]
print(nums)
for i in range(1, len(nums)):
    insert_value = nums[i]
    for j in range(i+1):
        if nums[j] > insert_value:
            for k in range(i, j, -1):
                nums[k] = nums[k-1]
            nums[j] = insert_value
            break
    print(i, nums)
print(nums)
