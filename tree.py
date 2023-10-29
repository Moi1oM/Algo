class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    # 기본 경우
    if root is None:
        return root

    # 재귀적으로 트리를 순회하면서 삭제할 노드를 찾습니다.
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        # 노드를 삭제합니다.
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # 두 자식이 모두 있는 경우, 오른쪽 서브트리에서 가장 작은 노드를 찾습니다.
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)

    return root

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

# 이진 검색 트리의 루트를 생성합니다.
root = TreeNode(50)

# 다음 값을 트리에 삽입합니다:
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder 순회 전의 트리:")
inorder(root)

# 키가 20인 노드를 삭제합니다.
root = deleteNode(root, 20)

print("\n키가 20인 노드 삭제 후 inorder 순회:")
inorder(root)

# 추가로 키가 30인 노드를 삭제합니다.
root = deleteNode(root, 30)

print("\n키가 30인 노드 삭제 후 inorder 순회:")
inorder(root)
