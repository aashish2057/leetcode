class Solution:
    def __init__(self):
        self.input = ""

    def letterCombos(self):
        digits = self.input
        phone = {"1": "","2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno","7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = [] 
        possible = []
        for n in digits:
            possible.append(phone[n])
        print(possible)
        def dfs(n, possible, number):
            if number and len(number) == n:
                res.append("".join(number))
                return
            for c in possible[0]:
                number.append(c)
                dfs(n, possible[1:], number)
                number.pop()
            
        dfs(len(digits), possible, [])
        return res

s = Solution()
print(s.letterCombos())
