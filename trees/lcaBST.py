class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def lca_on_bst(bst: Node, p:int, q:int) -> int:
    def dfs(bst: Node, p: int, q: int):
        if p < bst.val and q < bst.val:
            return dfs(bst.left, p, q)
        elif p > bst.val and q > bst.val:
            return dfs(bst.right, p, q)
        else:
            return bst.val

    return dfs(bst, p, q)

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

root = build_tree(iter("6 2 0 x x 4 3 x x 5 x x 8 7 x x 9 x x".split()), int)
res = lca_on_bst(root, 2, 8)
# print(" ".join(format_tree(root)))
print(res)
