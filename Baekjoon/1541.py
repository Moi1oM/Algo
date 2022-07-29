import sys
line = list(sys.stdin.readline().rstrip().split('-'))

res = 0
for i in range(len(line)):
    sik = list(line[i].split('+'))
    jung = 0
    for j in range(len(sik)):
        sik[j] = sik[j].lstrip('0')
        jung += eval(sik[j])
    if i == 0:
        res+=jung
    else:
        res-=jung
# res = eval(line[0])
# for i in range(1,len(line)):
    # if line[i][0]=='0':
    #     for j in range(len(line[i])):
    #         if line[i][j]!='0'
    # else:
    #     res-=eval(line[i])
print(res)