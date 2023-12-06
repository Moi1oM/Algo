from collections import deque
from itertools import combinations


def topological_sort(arr: list, teams: int, team_list: list) -> list:
    graph = [[] for _ in range(teams + 1)]
    indent = [0] * (teams + 1)
    for f, t in arr:
        graph[f].append(t)
        indent[t] += 1
    q = deque()
    for team in team_list:
        if indent[team] == 0:
            q.append(team)
    result = []
    while q:
        tmp = q.popleft()
        result.append(tmp)
        for x in graph[tmp]:
            indent[x] -= 1
            if indent[x] == 0:
                q.append(x)
    return result


N = int(input())
for _ in range(N):
    n = int(input())
    record = list(map(int, input().split()))
    change_n = int(input())
    changes = []
    changed_teams = set()
    for _ in range(change_n):
        change = list(map(int, input().split()))
        changed_teams.add(change[0])
        changed_teams.add(change[1])
        changes.append(change)

    flag = None
    for x, y in changes:
        x_record = record.index(x)
        y_record = record.index(y)
        if x_record < y_record:
            flag = True

    for x, y in combinations(changed_teams, 2):
        if [x, y] in changes or [y, x] in changes:
            continue
        x_record = record.index(x)
        y_record = record.index(y)
        if x_record < y_record:
            changes.append((x, y))
        else:
            changes.append((y, x))

    for x in changed_teams:
        index = record.index(x)
        record[index] = -1

    r = topological_sort(changes, n, list(changed_teams))

    for x in r:
        idx = record.index(-1)
        record[idx] = x
    if flag:
        print("IMPOSSIBLE")
    else:
        for x in record:
            print(x, end=" ")
        print()