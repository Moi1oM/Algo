import copy
n,k=map(int,input().split())
use=list(map(int,input().split()))
con=[]#콘센트에 현재 박혀있는 전자기기
count=0#몇번 바꿨는지에 대한 카운트
conlen=0#콘센트에 박혀있는 전자기기의 개수
nums=[0]*101#각 전자기기를 얼마나 사용하는지에 대한 배열
for i in use:
    nums[i]+=1
for i in range(k):
    if use[i] in con: #이번에 사용할 전자기기가 콘센트에 이미 박혀있으면 다음거로 넘어가기
        nums[use[i]]-=1 #사용은 한거니까 nums에서는 1빼주고
        continue
    elif conlen==n: #가장 많이 마주할 상황 다 꽂혀있을때 다음 사용해야할게 콘센트에 없음
        for j in range(n): #만약 콘센트에 꽂혀있는 것 중에 nums가 0 즉 앞으로 사용 안할 전자기기가 있다면 당장 그거를 빼고 사용해야할 전자기기를 추가함
            if nums[con[j]]==0:
                con.remove(con[j])
                con.append(use[i])
                nums[use[i]]-=1
                count+=1
                break
            if j==(n-1): #콘센트에 꽂혀있는 것 중에 nums가 0인게 없음
                ccount=0
                listb=copy.deepcopy(con) #콘센트에 꽂혀있는 전자기기를 listb에 복제
                for m in range(i,k): #use[i]이후에 사용해야 할 전자기기를 살펴보면서 콘센트에 박혀있는 것중 사용해야하는 거면 listb에서 제거시킴
                    if use[m] in listb:
                        listb.remove(use[m])
                    if len(listb)==1: #listb에 1개가 남았다면 그게 가장 덜 중요한 것이므로 그거를 콘센트에서 빼고 다음에 사용해야할 전자기기를 사용함
                        con.remove(listb[0])
                        con.append(use[i])
                        nums[use[i]]-=1
                        count+=1 #전자기기를 뽑은 횟수
                        break
    else: #맨 처음에 제한 없을때 conlen이 n까지 되도록 계속 증가시킴
        con.append(use[i]) #콘센트에 use[i]라는 전자기기를 추가
        conlen+=1 #콘센트에 박혀있는 전자기기의 수가 1씩 증가
        nums[use[i]]-=1 #한번씩 사용한 거니까 그 횟수를 줄여줌


print(count)