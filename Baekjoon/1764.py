import sys

n, m = map(int, sys.stdin.readline().split())
d = []
dd = []
for _ in range(n):
    d.append(sys.stdin.readline())
for _ in range(m):
    dd.append(sys.stdin.readline())
s1 = set(d)
s2 = set(dd)
s3 = list(s1 & s2)
s3.sort()
print(len(s3))
for i in range(len(s3)):
    print(s3[i], end="")
# cnt = 0
# d.sort()
# res = []
# for i in range(m):
#     a = sys.stdin.readline()
#     start = 0
#     end = n
#     while True:
#         mid = (start+end)//2
#         if a == d[mid]:
#             cnt += 1
#             res.append(a)
#             break
#         elif start >= end:
#             break
#         else:
#             index = 0
#             while True:
#                 if d[mid][index] != a[index]:
#                     break
#                 else:
#                     index += 1
#             if d[mid][index] > a[index]:
#                 end = mid-1
#             else:
#                 start = mid+1
#
# print(cnt)
# for i in res:
#     print(i)