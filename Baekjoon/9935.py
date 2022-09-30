import sys
key = sys.stdin.readline().rstrip()
explode = sys.stdin.readline().rstrip()
explode_len = len(explode)
res = ''
sindex = 0 - explode_len
findex = 0

for i in key:
    res = res + i
    sindex += 1
    findex += 1
#    print(sindex, findex, res)
    if len(res) >= explode_len:
        while True:
            if res[sindex:findex] == explode:
                sindex -= explode_len
                findex -= explode_len
                res = res[:-explode_len]
            else:
                break
if len(res)==0:
    print("FRULA")
else:
    print(res)
