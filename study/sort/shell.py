from random import randint

nums = [randint(1, 40) for _ in range(20)]
print(nums)

def shell_sort(arr):
    n = len(arr)
    gap = n // 2 # Initialize the gap
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2 # Reduce the gap size by half
shell_sort(nums)

print(nums)
