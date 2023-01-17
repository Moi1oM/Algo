import copy

def rotation_2d(old):
    a=len(old) #2
    b=len(old[0]) #3
    new=[[0]*a for _ in range(b)]
    for i in range(a): #0~1
        for j in range(b): #0~2
            new[j][a-1-i] = old[i][j]
    return new

def solution(key,lock):
    n = len(lock)
    m = len(key)
    new = [[0] * (n+2*m-2) for _ in range(n+2*m-2)]
    for i in range(m-1, n+m-1):
        for j in range(m-1, n+m-1):
            new[i][j] = lock[i-m+1][j-m+1]
    answer=True
    for _ in range(4):
        for i in range(n+m-1):
            for j in range(n+m-1):
                test = copy.deepcopy(new)
                for k in range(i,i+m):
                    for l in range(j, j+m):
                        test[k][l]+=key[k-i][l-j]
                answer = True
                for k in range(m-1,n+m-1):
                    for l in range(m-1,n+m-1):
                        if test[k][l]!=1:
                            answer = False
                if answer:
                    break
            if answer:
                break
        if not answer:
            key=rotation_2d(key)

    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))