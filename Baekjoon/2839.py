n = int(input())
if n>=5:
    d = [-1]*(n+1)
else:
    d = [-1]*6
d[3] = 1
d[5] = 1
for i in range(6, n+1):
    a = d[i-3]+1
    b = d[i-5]+1
    if a==0 and b==0:
        d[i]=-1
    elif a==0:
        d[i]=b
    elif b==0:
        d[i]=a
    else:
        d[i] = min(d[i-3]+1, d[i-5]+1)
print(d[n])