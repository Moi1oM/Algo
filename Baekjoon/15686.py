from itertools import combinations

n, m = map(int, input().split())
home = []
chicken = []

def cal_chickenlength(new_chicken):
    global home
    global m
    sol=[]
    for i in range(len(home)):
        minlength=987654321
        for j in range(m):
            length=abs(home[i][0]-new_chicken[j][0])+abs(home[i][1]-new_chicken[j][1])
            if length<minlength:
                minlength=length
        sol.append(minlength)
    return sum(sol)

def listing():
    global chicken
    global m
    l=[]
    ans=987654321
    for i in range(len(chicken)):
        l.append(i)
    for i in combinations(l,m):
        b=[]
        for j in range(m):
            b.append(chicken[i[j]])
        a=cal_chickenlength(b)
        if a<ans:
            ans=a
    return ans

for i in range(1,n+1):
    input_list = list(map(int, input().split()))
    for j in range(1,n+1):
        if input_list[j-1] == 1:
            home.append((i,j))
        if input_list[j-1] == 2:
            chicken.append((i,j))

print(listing())