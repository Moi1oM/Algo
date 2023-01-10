import sys
input = sys.stdin.readline

cap=2
n=2
deliveries=[0,0]
pickups=[0, 0]

def one_action(arr,cap,n):
    ret = 0
    now = cap
    for i in range(n-1,-1,-1):
        if ret == 0 and arr[i]!=0:
            ret = i+1
        if now >= arr[i] :
            now -= arr[i]
            arr[i] = 0
        else:
            arr[i] -= now
            now = 0
        if arr[i]==0:
            del arr[i]
            n-=1
        if now == 0:
            break
    return ret, n


def solution(cap, n, deliveries, pickups):
    answer = 0
    go_n = n
    out_n = n
    while True:
        go, go_n = one_action(deliveries, cap, go_n)
        out, out_n = one_action(pickups, cap, out_n)
        answer += 2*max(go, out)
        if go_n==0 and out_n==0:
            break
    return answer


print(solution(cap, n, deliveries, pickups))