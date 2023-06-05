from collections import defaultdict
class Solution:
    def __init__(self):
        self.s = "AABABBA"
        self.k = 1 

    def characterReplacement(self):
        maxSubstring = 0
        left, right = 0, 0
        swaps = self.k
        chars = defaultdict(int)
        elements, mainChar = 0, ''
        mainChar = self.s[left]
        while right < len(self.s):
            chars[self.s[right]] += 1
            if chars[self.s[right]] > chars[mainChar]:
                mainChar = self.s[right]
            elements += 1
            if elements - chars[mainChar] > swaps:
                break
            right += 1

        maxSubstring = max(maxSubstring, chars[mainChar] + swaps)
        return maxSubstring



s = Solution()
print(s.characterReplacement())
