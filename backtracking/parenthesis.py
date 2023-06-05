class Solution:
    def __init__(self):
        self.n = 3 

    def generate_parenthesis(self):
        n = self.n
        res = []
        def dfs(combo, n, leftN, rightN):
            if leftN == rightN == n:
                res.append("".join(combo))
                return
            
            if leftN < n:
                combo.append("(")
                dfs(combo, n, leftN+1, rightN)
                combo.pop()

            if rightN < leftN:
                combo.append(")")
                dfs(combo, n, leftN, rightN+1)
                combo.pop()
        dfs([], n, 0, 0)
        return res
s = Solution()
print(s.generate_parenthesis())
