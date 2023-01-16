#commands = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
#result is ["d", "EMPTY"]
#commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
#result is ["EMPTY", "group"]
#commands = ["UPDATE 1 1 a", "UPDATE 1 4 b", "UPDATE 2 1 c", "UPDATE 2 5 e", "MERGE 1 2 1 3", "MERGE 2 2 2 3", "MERGE 2 2 2 5","MERGE 1 3 2 5","UPDATE e i","UNMERGE 1 2","MERGE 1 2 2 1","MERGE 1 3 2 3", "UNMERGE 1 3"]


pyo = [[None]*51 for _ in range(51)]
merge_list = []

def unmerge_data(a, v):
    global pyo
    a=a.split(',')
    r = int(a[0][a[0].index('(')+1:])
    c = int(a[1][:a[1].index(')')])
    pyo[r][c]=v

def update_pyo(r,c,val):
    global pyo, merge_list
    is_new = True
    s1 = str((r,c))
    for l in range(len(merge_list)):
        mrg = merge_list[l].split("+")
        if s1 in mrg:
            is_new = False
            for it in mrg:
                unmerge_data(it, val)
    if is_new:
        pyo[r][c]=val



def print_pyo(r,c):
    global pyo
    if pyo[r][c]==None:
        return "EMPTY"
    else:
        return pyo[r][c]

def merge_pyo(r1,c1,r2,c2):
    global merge_list
    s1 = str((r1,c1))
    s2 = str((r2,c2))
    idx1 = None
    idx2 = None
    for l in range(len(merge_list)):
        mrg = merge_list[l].split("+")
        if s1 in mrg:
            idx1 = l
        if s2 in mrg:
            idx2 = l
    if idx1 != None and idx2 != None:
        merge_list.append(merge_list[idx1]+"+"+merge_list[idx2])
        if pyo[r1][c1]!=None:
            for i in merge_list[idx2].split("+"):
                unmerge_data(i, pyo[r1][c1])
        else:
            for i in merge_list[idx1].split("+"):
                unmerge_data(i, pyo[r2][c2])
        if idx1 < idx2 :
            idx1, idx2 = idx2, idx1
        merge_list.remove(merge_list[idx1])
        merge_list.remove(merge_list[idx2])
    elif idx1!=None:
        merge_list[idx1]+="+"+s2
        if pyo[r1][c1] != None:
            pyo[r2][c2] = pyo[r1][c1]
        elif pyo[r1][c1] == None and pyo[r2][c2] != None:
            for i in merge_list[idx1].split("+"):
                unmerge_data(i, pyo[r2][c2])
    elif idx2!=None:
        merge_list[idx2]+="+"+s1
        if pyo[r1][c1] != None:
            pyo[r2][c2] = pyo[r1][c1]
        elif pyo[r1][c1] == None and pyo[r2][c2] != None:
            for i in merge_list[idx2].split("+"):
                unmerge_data(i, pyo[r2][c2])
    else:
        merge_list.append(s1 + "+" + s2)
        if pyo[r1][c1] != None:
            pyo[r2][c2] = pyo[r1][c1]
        elif pyo[r1][c1] == None and pyo[r2][c2] != None:
            pyo[r1][c1] = pyo[r2][c2]



def unmerge_pyo(r,c):
    global merge_list
    s= str((r,c))
    for l in range(len(merge_list)):
        mrg = merge_list[l].split("+")
        if s in mrg:
            for it in mrg:
                if it == s:
                    continue
                else:
                    unmerge_data(it, None)
            merge_list.remove(merge_list[l])
            break

def update_all_pyo(v1,v2):
    global pyo
    for i in range(1,51):
        for j in range(1, 51):
            if pyo[i][j]==v1:
                pyo[i][j]=v2

def solution(commands):
    global pyo
    answer = []
    for command in commands:
        print(command)
        cmd = command.split()
        #print(cmd)
        if cmd[0]=="UPDATE":
            if len(cmd)==4:
                update_pyo(int(cmd[1]),int(cmd[2]),cmd[3])
            if len(cmd)==3:
                update_all_pyo(cmd[1],cmd[2])
        if cmd[0]=="MERGE":
            merge_pyo(int(cmd[1]),int(cmd[2]),int(cmd[3]),int(cmd[4]))
        if cmd[0]=="UNMERGE":
            unmerge_pyo(int(cmd[1]),int(cmd[2]))
        if cmd[0]=="PRINT":
            answer.append(print_pyo(int(cmd[1]),int(cmd[2])))
        for i in range(1,6):
            for j in range(1,6):
                print(pyo[i][j], end=" ")
            print()
        print("merge_list:",merge_list)
        print()
    return answer

print(solution(commands))