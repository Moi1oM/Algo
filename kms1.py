n=int(input())
m=int(input())
drinks=[[0]*n for _ in range(n)]
snacks=[[0]*m for _ in range(m)]
while True:
    input_text=input()
    if(input_text[0]=='d'):
        drinks[int(input_text[1])][int(input_text[2])]+=int(input_text[3:])
    elif (input_text[0]=='s'):
        snacks[int(input_text[1])][int(input_text[2])]+=int(input_text[3:])
    elif (input_text[0]=='n'):
        break
    else:
        print("Wrong Input")
print(drinks)
print(snacks)