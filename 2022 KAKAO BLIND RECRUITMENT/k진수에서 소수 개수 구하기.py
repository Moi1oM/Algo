k_nary_num = ""
import math
def make_k_nary(n,k):
    global k_nary_num
    while n>0:
        k_nary_num += str(n%k)
        n = n//k
    k_nary_num = "".join(reversed(k_nary_num))
def is_prime(n):
    res = True
    if n <= 1:
        return False
    for i in range(2,n):
        if n%i==0:
            res = False
            break
    return res

def is_zero(s):
    if s=='0' or s=='s' or s=='e':
        return True
    else:
        return False

def solution(n, k):
    global k_nary_num
    answer = 0
    make_k_nary(n,k)
    print(k_nary_num)
    iters = k_nary_num.split("0")
    for num in iters:
        if num == "":
            continue
        if is_prime(int(num)):
            answer+=1
    # k_nary_num += "e"
    # for l in range(1,len(k_nary_num)-1):
    #     s_index = 1
    #     f_index = s_index + l - 1
    #     while f_index < len(k_nary_num)-1:
    #         checking = k_nary_num[s_index:f_index+1]
    #         if not "0" in checking and is_zero(k_nary_num[s_index-1]) and is_zero(k_nary_num[f_index+1]):
    #             flag = is_prime(int(checking))
    #             if flag:
    #                 #print(checking)
    #                 answer += 1
    #         s_index += 1
    #         f_index += 1

    return answer


print("answer is",solution(437674, 3))