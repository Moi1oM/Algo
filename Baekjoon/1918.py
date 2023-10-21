line = input()


class Stack:
    def __init__(self):
        self._main_list = []
        self.length = 0

    def push(self, item):
        self._main_list.append(item)
        self.length += 1

    def peek(self):
        return self._main_list[self.length - 1]

    def pop(self):
        self.length -= 1
        return self._main_list.pop()


def is_big_alphabet(character: str):
    if "A" <= character <= "Z":
        return True
    return False


def check_priority(now, stack_top):
    priority = {"+" : 3, "-" : 3, "*" : 2, "/" : 2, "(" : 1, ")" : 1}
    now_p = priority[now]
    stack_top_p = priority[stack_top]
    return now_p < stack_top_p

stack = []
for x in line:
    if is_big_alphabet(x):
        # pass
        print(x, end="")
    else: # 기호일 떄
        if not stack:
            stack.append(x)
        elif x == "(":
            stack.append(x)
        elif x == ")":
            while True:
                now = stack.pop()
                if now == "(":
                    break
                print(now, end="")
        elif check_priority(x, stack[len(stack) - 1]):
            stack.append(x)
        else:
            while stack:
                now = stack.pop()
                if now == "(":
                    stack.append(now)
                    break
                if check_priority(x, now):
                    stack.append(now)
                    break
                else:
                    # pass
                    print(now, end="")
            stack.append(x)
    # print(x, stack)

while stack:
    print(stack.pop(), end="")
