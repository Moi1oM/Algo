# commands = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
# result is ["d", "EMPTY"]
commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice",
            "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta",
            "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik",
            "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
# result is ["EMPTY", "group"]
# commands = ["UPDATE 1 1 a", "UPDATE 1 4 b", "UPDATE 2 1 c", "UPDATE 2 5 e", "MERGE 1 2 1 3", "MERGE 2 2 2 3", "MERGE 2 2 2 5","MERGE 1 3 2 5","UPDATE e i","UNMERGE 1 2","MERGE 1 2 2 1","MERGE 1 3 2 3", "UNMERGE 1 3"]

pyo = [None] * 2500
state = list(range(2500))


def find_index(r, c):
    return (int(r) - 1) * 50 + (int(c) - 1)


def update_one(idx, val):
    if state[idx] == None:
        pyo[idx] = val
    else:
        for i in range(2500):
            if state[i] == state[idx]:
                pyo[i] = val


def update_all(v1, v2):
    global pyo
    for i in range(2500):
        if pyo[i] == v1:
            pyo[i] = v2


def merge(idx1, idx2):
    val = None
    old_state = state[idx2]
    for i in range(2500):
        if state[i]==old_state:
            state[i]=state[idx1]
    # if state[idx1] == None and state[idx2] == None:
    #     state[idx1] = state[2500]
    #     state[idx2] = state[2500]
    #     state_val = state[2500]
    #     state[2500] += 1
    #
    # elif state[idx1] == None:
    #     state[idx1] = state[idx2]
    #     state_val = state[idx2]
    #
    # elif state[idx2] == None:
    #     state[idx2] = state[idx1]
    #     state_val = state[idx1]
    #
    # else:
    #     s = state[idx2]
    #     for i in range(2500):
    #         if state[i] == s:
    #             state[i] = state[idx1]
    #     state_val = state[idx1]

    if pyo[idx1] != None:
        val = pyo[idx1]
    elif pyo[idx2] != None:
        val = pyo[idx2]

    if val:
        for i in range(2500):
            if state[i] == state[idx1]:
                pyo[i] = val


def unmerge(idx):
    old_v = state[idx]
    for i in range(2500):
        if state[i] == old_v:
            state[i]=i
            if i == idx:
                continue
            pyo[i] = None


def answer_print(idx):
    if pyo[idx] == None:
        return "EMPTY"
    else:
        return pyo[idx]


def solution(commands):
    global pyo
    answer = []
    for line in commands:
        command, *tokens = line.split()
        if command == "UPDATE":
            if len(tokens) == 3:
                update_one(find_index(tokens[0], tokens[1]), tokens[2])
            if len(tokens) == 2:
                update_all(tokens[0], tokens[1])
        if command == "MERGE":
            merge(find_index(tokens[0], tokens[1]), find_index(tokens[2], tokens[3]))
        if command == "UNMERGE":
            unmerge(find_index(tokens[0], tokens[1]))
        if command == "PRINT":
            answer.append(answer_print(find_index(tokens[0], tokens[1])))
        print(line)
        for i in range(1, 6):
            for j in range(1, 6):
                print(pyo[find_index(i, j)], end=" ")
            print()
        print()
    return answer


print(solution(commands))
