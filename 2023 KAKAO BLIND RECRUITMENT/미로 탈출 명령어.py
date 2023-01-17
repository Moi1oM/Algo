def solution(n, m, x, y, r, c, k):
    direction=['d','l','r','u']
    move = [0,0,0,0]
    partner = [3,2,1,0]
    p_move = [(1,0),(0,-1),(0,1),(-1,0)]
    add_move=[0,0,0,0]
    def isit_possible(x, y):
        res = True
        if x<=0 or y<=0 or x>n or y>m:
            res=False
        return res

    def solve():
        answer=''
        short_len = abs(x-r)+abs(y-c)
        g_move = k-short_len
        if g_move<0 or g_move%2!=0:
            answer='impossible'
            return answer
        if r-x < 0:
            move[3]+=abs(r-x)
        if r-x > 0:
            move[0]+=abs(r-x)
        if c-y < 0:
            move[1]+=abs(c-y)
        if c-y > 0:
            move[2]+=abs(c-y)
        current_x = x
        current_y = y
        if g_move==0:
            for i in range(4):
                answer+=direction[i]*move[i]
        else:
            while True:
                if max(move)==0 and g_move==0 and max(add_move)==0:
                    break
                move_idx = 5
                for i in range(4):
                    if move[i]:
                        move_idx = i
                        break
                    if i==3:
                        move_idx = 3
                        break
                add_move_idx = 5
                if g_move>0:
                    for i in range(4):
                        px = current_x + p_move[i][0]
                        py = current_y + p_move[i][1]
                        if isit_possible(px, py):
                            add_move_idx = i
                            break
                else:
                    for i in range(4):
                        if add_move[i]:
                            px = current_x + p_move[i][0]
                            py = current_y + p_move[i][1]
                            if isit_possible(px,py):
                                add_move_idx = i
                                break
                        if i==3:
                            add_move_idx=3
                if move_idx <= add_move_idx and max(move)!=0:
                    answer += direction[move_idx]
                    current_y += p_move[move_idx][1]
                    current_x += p_move[move_idx][0]
                    move[move_idx] -= 1
                elif g_move>0:
                    g_move-=2
                    answer += direction[add_move_idx]
                    add_move[partner[add_move_idx]]+=1
                    current_y = py
                    current_x = px
                else:
                    answer+=direction[add_move_idx]
                    current_y += p_move[add_move_idx][1]
                    current_x += p_move[add_move_idx][0]
                    add_move[add_move_idx]-=1
                # print(current_x,current_y,move,move_idx, add_move, add_move_idx,g_move)
                # print(answer)
                # print()
        return answer

    return solve()

print(solution(2,2,1,1,2,2,2))