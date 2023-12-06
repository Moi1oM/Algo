def find(parent: list, x: int) -> int:
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(a: int, b: int, parent: list) -> None:
    parent_a = find(parent, a)
    parent_b = find(parent, b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


parent = [i for i in range(7)]
print(parent)
print(find(parent, 1), find(parent, 2))
union(1, 2, parent)
union(1, 3, parent)
print(parent)
union(4, 5, parent)
union(5, 6, parent)
print(parent)
union(5, 3, parent)
print(parent)
find(parent, 6)
print(parent)