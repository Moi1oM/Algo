def solution(food_times, k):
    index=0
    count=0
    while(count<k):
        if(food_times[index]>0):
            food_times[index]-=1
            index+=1
            count+=1
        elif(food_times[index]==0):
            index+=1
        if index>=len(food_times):
            index=0
        if(count==k):
            mcount=0
            while(True):
                if(food_times[index]>0):
                    print(food_times[index], index, food_times)
                    break
                index+=1
                mcount+=1
                if(index>=len(food_times)):
                    index=0
                if(mcount==len(food_times)):
                    index=-2
                    break
    return index+1
print(solution([3,1,2],5))