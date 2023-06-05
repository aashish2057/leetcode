from collections import deque

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node):
    res = []
    queue = deque([root])

    while len(queue) > 0:
        new = []
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            new.append(node.val)
            if i%2 != 0:
                for child in [node.right, node.left]:
                    if child is not None:
                        queue.append(child)
            else:
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
        res.append(new)
    return res



def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

root = build_tree(iter("1 2 4 x 7 x x 5 x x 3 x 6 x x".split()), int)
res = 0
if type(root) == Node:
    res = level_order_traversal(root)
print(res)
