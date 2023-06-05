class Solution:
    def __init__(self):
        self.columnTitle = "AAA"

    def titleToNumber(self):
        columnTitle = self.columnTitle
        columnNumber = 0
        for i, c in enumerate(reversed(columnTitle)):
            number = ord(c) - ord("A") + 1
            columnNumber += pow(26, i) * number
        return columnNumber
s = Solution()
print(s.titleToNumber())
