class Solution:
    def __init__(self):
        self.s = "abc"

    def permutations(self):
        s = set(self.s)
        res = []

        def dfs(used: set, permutation, s):
            if used and len(used) == len(s):
                res.append("".join(permutation))
                return
            
            for c in s:
                if c not in used:
                    permutation.append(c)
                    used.add(c)
                    dfs(used, permutation, s)
                    permutation.pop()
                    used.remove(c)
            
        dfs(set(), [], s)
        return res

s = Solution()
print(s.permutations())
