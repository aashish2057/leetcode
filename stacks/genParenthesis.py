class Parenthesis:
    def __init__(self) -> None:
        self.n = 8 
    def generateParenthesis(self):
        res = []
        stack = []
        def dfs(openN, closingN):
            if closingN == self.n and openN == self.n:
                res.append(''.join(stack))
                return
            if closingN < openN:
                stack.append(')')
                dfs(openN, closingN+1)
                stack.pop()
            if openN < self.n:
                stack.append('(')
                dfs(openN+1, closingN)
                stack.pop()
        dfs(0, 0)
        return res

p = Parenthesis() 
print(p.generateParenthesis())
