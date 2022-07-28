import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline()
checking = 'T' + s[:(2*n)]
answer = 'I'
nn=2*n+2
for i in range(2, nn):
    if i%2==1:
        answer = answer+'I'
    else:
        answer = answer+'O'
start = 0
end = 2*n
cnt = 0
for _ in range(m-(2*n)):
    checking=checking[1:]+s[end]
    if checking == answer:
        cnt+=1
    start+=1
    end+=1
print(cnt)