import copy
n,k=map(int,input().split())
use=list(map(int,input().split()))
con=[]
count=0
conlen=0
nums=[0]*101
for i in use:
    nums[i]+=1
#print(use)
#print(con,nums)
for i in range(k):
#    print(i,con,use,nums)
    if use[i] in con:
        nums[use[i]]-=1
#        print("1번",i,con,use,nums)
        continue
    elif conlen==n:
        for j in range(n):
            if nums[con[j]]==0:
                con.remove(con[j])
                con.append(use[i])
                nums[use[i]]-=1
                count+=1
#                print("2번",i,con,use,nums)
                break
            if j==(n-1):
                ccount=0
                listb=copy.deepcopy(con)
#                print(i,j,listb,con)
                for m in range(i,k):
                    if use[m] in listb:
                        listb.remove(use[m])
#                        print("m ",m,listb)
                    if len(listb)==1:
#                        print(con,listb[0])
                        con.remove(listb[0])
                        con.append(use[i])
                        nums[use[i]]-=1
#                        print(i,con,use,nums)
                        count+=1
                        break
    else:
        con.append(use[i])
        conlen+=1
        nums[use[i]]-=1


print(count)