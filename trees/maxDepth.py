class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def tree_max_depth(root: Node) -> int:
    def dfs(root):
        if root is None:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)
        return (max(left, right) + 1)
    return dfs(root) - 1 if root else 0

    return max(left, right)
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

root = build_tree(iter("5 4 3 x x 8 x x 6 x x".split()), int)
res = tree_max_depth(root)
print(res)
