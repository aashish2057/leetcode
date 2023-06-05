class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balanced(root: Node) -> int:
    def dfs(root):
        if root is None:
            return [-1, True]

        left = dfs(root.left)
        right = dfs(root.right)
        balanced = False
        if left[1] and right[1] and abs(left[0] - right[0]) <= 1:
            balanced = True
        print(root.val, left[0], right[0], balanced)
        return [max(left[0], right[0]) + 1, balanced]

    return dfs(root)


def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


root = build_tree(iter("1 2 4 x 7 x x 5 x x 3 x 6 x x".split()), int)
res = balanced(root)
print(res)
