n=int(input())

d=[1,1]
if(n==0):
    print(0)
elif(n<=2):
    print(d[n-1])
else:
    for i in range(n-2):
        d.append(d[i]+d[i+1])
    print(d[n-1])