class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def valid_bst(root: Node) -> bool:
    def dfs(root, minNode, maxNode):
        if root is None:
            return True
        
        if not (minNode < root.val < maxNode):
            return False

        return dfs(root.left, minNode, root.val) and dfs(root.right, root.val, maxNode)
        
    return dfs(root, float("-inf"), float("inf"))



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

root = build_tree(iter("6 4 3 x x 8 x x 8 x x".split()), int)
res = valid_bst(root)
print(res)
# print(" ".join(format_tree(root)))
