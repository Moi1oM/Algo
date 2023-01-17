numbers = [7, 42, 5]
# answer is [1, 1, 0]

def is_tree(tree, p):
    if p == "0":
        res = True
        for i in tree:
            if i == "1":
                res = False
                break
        return res
    if len(tree)==1:
        return True
    l = len(tree)
    c = l // 2
    return is_tree(tree[:c],tree[c]) and is_tree(tree[c+1:], tree[c])

def solution(numbers):
    answer = []
    for num in numbers:
        binary_num = bin(num)
        binary_num = binary_num[2:]
        idx = 1
        while True:
            if idx>=len(binary_num):
                break
            idx=idx*2+1
        binary_num = "0"*(idx-len(binary_num))+binary_num
        part = binary_num[idx//2]
        if is_tree(binary_num,part):
            answer.append(1)
        else:
            answer.append(0)
    return answer

print(solution(numbers))