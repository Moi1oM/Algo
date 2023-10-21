n = int(input())
tree = []
for _ in range(n):
    tree.append(input().split())


class Node:
    trees = {}

    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

    def preorder(self):
        print(self.root, end="")
        if self.left != ".":
            Node.preorder(Node.trees[self.left])

        if self.right != ".":
            Node.preorder(Node.trees[self.right])

    def inorder(self):
        if self.left != ".":
            Node.inorder(Node.trees[self.left])
        print(self.root, end="")
        if self.right != ".":
            Node.inorder(Node.trees[self.right])

    def postorder(self):
        if self.left != ".":
            Node.postorder(Node.trees[self.left])
        if self.right != ".":
            Node.postorder(Node.trees[self.right])
        print(self.root, end="")


for root, l, r in tree:
    Node.trees[root] = Node(root, l, r)

Node.preorder(Node.trees["A"])
print()
Node.inorder(Node.trees["A"])
print()
Node.postorder(Node.trees["A"])