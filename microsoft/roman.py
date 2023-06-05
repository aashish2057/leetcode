class Solution:
    def __init__(self):
        self.s = "MCMXCIV"

    def romanToInt(self):
        s = self.s

        roman = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        sum = 0
        for i,c in enumerate(s):
            if c == "I" and i+1 < len(s) and s[i+1] in "VX":
                sum -= 1
                continue
            if c == "X" and i+1 < len(s) and s[i+1] in "LC":
                sum -= 10 
                continue
            if c == "C" and i+1 < len(s) and s[i+1] in "DM":
                sum -= 100 
                continue
            sum += roman[c]
        return sum

s = Solution()
print(s.romanToInt())

