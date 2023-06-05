class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: Node) -> int:
    res = [0]

    def dfs(root):
        if root is None:
            return 0
        
        res[0] += 

        return dfs(root.left) + dfs(root.right) + 1 
        
    print(dfs(root))
    return res[0]

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

root = build_tree(iter("1 2 4 x x 5 x x 3 x x".split()), int)
if root:
    res = diameterOfBinaryTree(root)
    print(res)
