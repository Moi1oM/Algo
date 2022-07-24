n=int(input())
plusidx=6
cnt=1
index=1
while True:
    if index >= n:
        break
    index+=plusidx
    plusidx+=6
    cnt+=1
print(cnt)