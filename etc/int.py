N=int(input())
M=int(input())
a=0
for _ in range(N):
    print(int(M%10))
    a+=int(M%10)
    M//=10
    print(M)
print(int(a))