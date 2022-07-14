d=[[-1]*15 for _ in range(5)]
max_len=0
for j in range(5):
    INPUT=input()
    if max_len<len(INPUT):
        max_len=len(INPUT)
    for i in range(len(INPUT)):
        d[j][i]=INPUT[i]

for i in range(max_len):
    for j in range(5):
        if(d[j][i]!=-1):
            print(d[j][i], end="")