import sys
n = int(sys.stdin.readline().rstrip())
nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
m = int(sys.stdin.readline().rstrip())
findings = list(map(int,sys.stdin.readline().split()))
res = []
dix = [0]*
for i in range(n):

#
#
# def binary(num):
#     check = False
#     start = 0
#     end = n-1
#     while True:
#         mid = (start + end) // 2
#         if num == nums[mid]:
#             check = True
#             break
#         elif start >= end:
#             break
#         elif num < nums[mid]:
#             end = mid-1
#         else:
#             start = mid+1
#     if check:
#         return nums.count(num)
#     else:
#         return -1
#
# def checking_front(idx):
#     check = nums[idx]
#     cnt = 0
#     for i in range(idx-1,-1,-1):
#         if nums[i] == check:
#             cnt+=1
#         else:
#             break
#     return cnt
#
# def checking_back(idx):
#     check = nums[idx]
#     cnt = 0
#     for i in range(idx+1,n):
#         if nums[i] == check:
#             cnt+=1
#         else:
#             break
#     return cnt
#
#
# for i in findings:
#     index = binary(i)
#     if index == -1:
#         res.append(0)
#     else:
#         res.append(index)
#
# for i in res:
#     print(i, end=" ")
