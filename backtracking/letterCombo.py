class Solution:
    def __init__(self):
        self.n = 4 

    def letter_combination(self):
        res = []
        def dfs(n, word):
            if word and len(word) == n:
                res.append("".join(word))
                return
            word.append("a")
            dfs(n, word)
            word.pop()
            word.append("b")
            dfs(n,word)
            word.pop()
        dfs(self.n, [])
        return res

s = Solution()
print(s.letter_combination())
