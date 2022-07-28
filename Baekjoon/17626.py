n = int(input())
d= [-1] * 50001
res = []
for i in range(1,50001):
    d[i] = i
for i in range(2,251):
    a = i**2
    res.append(a)
    if a >50000:
        break
    d[i**2] = 1
for i in res:
    idx = 1
    while True:
