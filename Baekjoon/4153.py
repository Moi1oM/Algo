while True:
    d = list(map(int, input().split()))
    if d[0] == 0 and d[1] == 0 and d[2] == 0:
        break
    d.sort()
    if d[2]**2 == d[1]**2 + d[0]**2:
        print("right")
    else:
        print("wrong")