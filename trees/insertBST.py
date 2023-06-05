class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def insert_bst(root: Node, val: int):
    def dfs(root, val):
        if root is None:
            return Node(val)

        if val < root.val:
            root.left = dfs(root.left, val)
        else:
            root.right = dfs(root.right, val)
    return dfs(root, val) 

def format_tree(node):
    if node is None:
        yield 'x'
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

root = build_tree(iter("".split()), int)
res = insert(root, 7)
# print(res)
print(" ".join(format_tree(root)))
