class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def visiable_tree_nodes(root: Node) -> int:
    visable = [0]
    def dfs(root, highest):
        if root is None:
            return
        
        if root.val >= highest:
            visable[0] += 1
        

        dfs(root.left,max(highest, root.val))
        dfs(root.right,max(highest, root.val))
    dfs(root, float("-inf"))
    return visable[0]


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

root = build_tree(iter("5 4 3 x x 8 x x 6 x x".split()), int)
res = visiable_tree_nodes(root)
print(res)
