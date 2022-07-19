n=int(input())
for _ in range(n):
    a,b,c=map(int,input().split())
    if a == 1:
        print(100+c)
    print((c%a)*100+(c//a)+1)