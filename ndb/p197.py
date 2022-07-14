import sys
n=int(input())
array=list(list(map(int,input().split())))
array.sort()
m=int(input())
input_data=list(map(int,input().split()))

# 순차 탐색
# for i in input_data:
#     check=0
#     for j in range(len(array)):
#         if(i==array[j]):
#             check=1
#             print("yes", end=" ")
#             break
#     if check==0:
#         print("no", end=" ")

# 이진 탐색
# def binary_search(array, target, start, end):
#     mid=(start+end)//2
#     if start>end:
#         return None
#     if array[mid]==target:
#         return mid
#     elif array[mid]>target:
#         return binary_search(array,target,start,mid-1)
#     else:
#         return binary_search(array,target,mid+1,end)
# print(array)
# for i in input_data:
#     result=binary_search(array,i,0,n-1)
#     if result!=None:
#         print("yes", end=" ")
#     else:
#         print("no", end=" ")

#계수 정렬
