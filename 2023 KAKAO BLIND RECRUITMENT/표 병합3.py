commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice",
            "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta",
            "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik",
            "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]

def solution(commands):
    def rc2index(r, c):
        return (int(r) - 1) * 50 + int(c) - 1

    def update(p, s):
        old_state = states[p]
        for index in range(length):
            if states[index] == old_state:
                table[index] = s

    def replace(s1, s2):
        for index in range(length):
            if table[index] == s1:
                table[index] = s2

    def merge(p1, p2):
        change = None
        if table[p1] != 'EMPTY' and table[p2] == 'EMPTY':
            change = table[p1]
        elif table[p1] == 'EMPTY' and table[p2] != 'EMPTY':
            change = table[p2]
        elif table[p1] != 'EMPTY' and table[p2] != 'EMPTY':
            change = table[p1]
        old_state = states[p2]
        for index in range(length):
            if states[index] == old_state:
                states[index] = states[p1]
        if change:
            for index in range(length):
                if states[index] == states[p1]:
                    table[index] = change

    def unmerge(p):
        old_value = table[p]
        old_state = states[p]
        for index in range(length):
            if states[index] == old_state:
                states[index] = index
                table[index] = 'EMPTY'
        table[p] = old_value

    def print_(p):
        answer.append(table[p])

    def solve():
        for line in commands:
            command, *tokens = line.split()
            if command == 'UPDATE':
                if len(tokens) > 2:
                    update(rc2index(tokens[0], tokens[1]), tokens[2])
                else:
                    replace(tokens[0], tokens[1])
            elif command == 'MERGE':
                merge(rc2index(tokens[0], tokens[1]), rc2index(tokens[2], tokens[3]))
            elif command == 'UNMERGE':
                unmerge(rc2index(tokens[0], tokens[1]))
            elif command == 'PRINT':
                print_(rc2index(tokens[0], tokens[1]))

    length = 2500
    answer = []
    table = ['EMPTY'] * length
    states = list(range(length))
    solve()
    return answer

print(solution(commands))