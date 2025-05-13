#  Lowest Common Ancestor in BST
def find_lca_bst(root, p, q):
    while root:
        if p < root.value and q < root.value:
            root = root.left
        elif p > root.value and q > root.value:
            root = root.right
        else:
            return root.value
    return None

# Test case
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

bst = BinarySearchTree()
for val in [20, 10, 30, 5, 15, 25, 35]:
    bst.insert(val)

print("LCA of 5 and 15:", find_lca_bst(bst.root, 5, 15))  # 10
print("LCA of 5 and 25:", find_lca_bst(bst.root, 5, 25))  # 20
print("LCA of 25 and 35:", find_lca_bst(bst.root, 25, 35))  # 30