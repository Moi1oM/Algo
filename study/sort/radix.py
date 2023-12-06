from random import randint
from copy import deepcopy

nums = [randint(1, 40) for _ in range(20)]
print("before sort : ", nums)

bucket = [[] for _ in range(10)]
index = 1
max_num = max(nums)
max_index = 0
while max_num:
    max_num //= 10
    max_index += 1

def calculate_bucket_index(num, index):
    for _ in range(index - 1):
        num = num // 10
    return num % 10


new_nums = deepcopy(nums)
print("before", max_index, new_nums)
while index <= max_index:
    for x in new_nums:
        bucket_index = calculate_bucket_index(x, index)
        bucket[bucket_index].append(x)
    new_nums = []
    for x in bucket:
        new_nums.extend(x)
    bucket = [[] for _ in range(10)]

    print(index, new_nums)
    index += 1



print("after sort : ", new_nums)
