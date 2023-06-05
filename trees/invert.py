class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def invert(root: Node):

    if root is None:
        return
    tmp = root.left
    root.left = root.right
    root.right = tmp
    invert(root.left)
    invert(root.right)

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

root = build_tree(iter("1 2 4 x x 5 6 x x x 3 x x".split()), int)
res = invert(root)
print(" ".join(format_tree(root)))
