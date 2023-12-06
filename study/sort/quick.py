from random import randint

nums = [randint(1, 40) for _ in range(20)]
print("before sort: ", nums)


def quicksort(arr: list, lo: int, hi: int)->None:
    def partition(arr: list, lo: int, hi: int) -> int:
        pivot = arr[hi]
        left = lo
        for right in range(lo, hi):
            if arr[right] < pivot:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
        arr[left], arr[hi] = arr[hi], arr[left]
        return left

    if lo < hi:
        pivot = partition(arr, lo, hi)
        quicksort(arr, lo, pivot - 1)
        quicksort(arr, pivot + 1, hi)


quicksort(nums, 0, len(nums)-1)
print("after sort: ", nums)
