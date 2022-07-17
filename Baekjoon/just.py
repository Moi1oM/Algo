a=input()
index=-1
check=True

d=[]
def isLeftnum():
    global index
    global d
    if index==0:
        return 0
    elif d[index-1]=="(" or d[index-1]=="[":
        return 0
    else:
        d[index-1]=d[index-1]+d[index]
        d.pop()
        index-=1
        return isLeftnum()

#print(len(a))
for i in range(len(a)):

    if a[i]=="(" or a[i]==")" or a[i]=="[" or a[i]=="]":
        d.append(a[i])
        index+=1
 #       print(check,d,"index: ",index," i: ",i)

        if a[i]==")":
            if index>=1 and d[index-1]=="[":
                check=False
                break

            elif index>=1 and  d[index-1]=="(":
                d.pop()
                d.pop()
                index-=1
                d.append(2)
                isLeftnum()
            elif index>=2 and  d[index-2]=="[":
                check=False
                break

            elif index>=2 and  d[index-2]=="(":
                tmp=d[index-1]*2
                d.pop()
                d.pop()
                d.pop()
                d.append(tmp)
                index-=2
 #               print(check,d,"index: ",index," i: ",i)
                isLeftnum()
            else:
                check=False
                break
        if a[i]=="]":
            if index>=1 and  d[index-1]=="(":
                check=False
                break
            elif index>=1 and  d[index-1]=="[":
                d.pop()
                d.pop()
                index-=1
                d.append(3)
                isLeftnum()

            elif index>=2 and  d[index-2]=="(":
                check=False
                break

            elif index>=2 and  d[index-2]=="[":
                tmp=d[index-1]*3
                d.pop()
                d.pop()
                d.pop()
                d.append(tmp)
                index-=2
                isLeftnum()
            else:
                check=False
                break
#        print(check,d,"index: ",index," i: ",i)
    else:
        check=False
        break
if index!=0:
    check=False
elif d[0]=="(" or d[0]=="[" or d[0]==")" or d[0]=="]" :
    check=False
if check:
    print(d[0])
else:
    print(0)