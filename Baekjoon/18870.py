n = int (input())
d = []
m = list(map(int, input().split()))
index = 0
for i in m:
    d.append((i,index))
    index+=1

d.sort()
res=[0]*n
for i in range(n):
    if i == 0:
        res[d[i][1]] = i
    else:
        j=0
        for j in range(i-1,-1,-1):
            if d[i][0] != d[j][0]:
                break
            if j == 0:
                j = 0
                break
        res[d[i][1]] = j+1
print(d)
print(res)