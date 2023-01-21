line = input()
stack = []

def is_alpha(s):
    if s=='+' or s=='-' or s=='*' or s=='/' or s=='(' or s==')':
        return False
    else:
        return True

for one in line:
    if not is_alpha(one): #기호일때
        if one == '(':
            stack.append(one)

        if one == ')':
            while True:
                now = stack.pop()
                if now == '(':
                    break
                else:
                    print(now, end="")

        if one == '+' or one == '-':
            while stack and stack[-1]!='(':
                print(stack[-1],end="")
                stack.pop()
            stack.append(one)

        if one == '*' or one == '/':
            while stack and (stack[-1]=='*' or stack=='/'):
                print(stack[-1], end="")
                stack.pop()
            stack.append(one)
    else: #알파벳일때
        print(one, end="")

    #print(one, stack)

while stack:
    now = stack.pop()
    print(now, end="")