n, k = map(int, input().split())
la=max(n,k)
per=[[-1]*(la+1) for _ in range(la+1)]
def calper(nn,kk):
    if per[nn][kk]!=-1:
        return per[nn][kk]
    elif nn==kk or kk==0:
        per[nn][kk]=1
        return per[nn][kk]
    else:
        per[nn][kk]=calper(nn-1,kk-1)+calper(nn-1,kk)
        return per[nn][kk]
mi=min(n,k)
sum=0
for i in range(1,mi+1):
    sum+=calper(n-1,i-1)*calper(k,i)
print(sum%1000000000)