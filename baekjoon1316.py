def f(word):
    checking_alphabet=[0]*26
    return_val=1
    for i in range(len(word)):
        alphabet=int(ord(word[i]))-int(ord('a'))
        if(checking_alphabet[alphabet]==0):
            checking_alphabet[alphabet]=1
            continue
        elif(checking_alphabet[alphabet]==1 and word[i-1]==word[i]):
            continue
        else:
            return_val=0
    return return_val
N=int(input())
count=0
for _ in range(N):
    count+=f(input())
print(count)