# N=int(input())
# d=[[0]*10 for _ in range(26)]
# print(d)
# for i in range(N):
#     INPUT=input()
#     for j in reversed(range(len(INPUT))):
#         alphabet=int(ord(INPUT[j]))-int(ord('A'))
#         d[alphabet][j]+=1
N=int(input())
d=[0]*26
for i in range(N):
    INPUT=input()
    for j in range(len(INPUT)):
        alphabet=int(ord(INPUT[j]))-int(ord('A'))
        d[alphabet]=d[alphabet]+10**(len(INPUT)-j-1)
d.sort(reverse=True)
ans=0
for i in range(len(d)):
    ans+=d[i]*(9-i)
print(ans)

# alphabet=int(ord(word[i]))-int(ord('A'))