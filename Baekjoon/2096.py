n = int(input())
max_score = [[0] * 3 for _ in range(2)]
min_score = [[0] * 3 for _ in range(2)]

for _ in range(n):
    line = list(map(int, input().split()))
    max_score[1][0] = line[0] + max(max_score[0][0], max_score[0][1])
    max_score[1][1] = line[1] + max(max_score[0][0], max_score[0][1], max_score[0][2])
    max_score[1][2] = line[2] + max(max_score[0][1], max_score[0][2])
    min_score[1][0] = line[0] + min(min_score[0][0], min_score[0][1])
    min_score[1][1] = line[1] + min(min_score[0][0], min_score[0][1], min_score[0][2])
    min_score[1][2] = line[2] + min(min_score[0][1], min_score[0][2])
    for i in range(3):
        max_score[0][i] = max_score[1][i]
        min_score[0][i] = min_score[1][i]
print(max(max_score[0]), min(min_score[0]))

'''
mapping = []
max_score = [[0]*3 for _ in range(n)]
min_score = [[0]*3 for _ in range(n)]

for _ in range(n):
    line = list(map(int,input().split()))
    mapping.append(line)

for i in range(3):
    max_score[0][i]=mapping[0][i]
    min_score[0][i]=mapping[0][i]

for i in range(1, n):
    max_score[i][0] = mapping[i][0] + max(max_score[i - 1][0], max_score[i - 1][1])
    max_score[i][2] = mapping[i][2] + max(max_score[i - 1][1], max_score[i - 1][2])
    max_score[i][1] = mapping[i][1] + max(max_score[i - 1][0], max_score[i - 1][1], max_score[i-1][2])
    min_score[i][0] = mapping[i][0] + min(min_score[i - 1][0], min_score[i - 1][1])
    min_score[i][2] = mapping[i][2] + min(min_score[i - 1][1], min_score[i - 1][2])
    min_score[i][1] = mapping[i][1] + min(min_score[i - 1][0], min_score[i - 1][1], min_score[i - 1][2])

print(max(max_score[n-1]), min(min_score[n-1]))
'''
