from collections import defaultdict


class Solution:
    def __init__(self):
        self.nums = [2,7,11,15]
        self.target = 9

    def twoSum(self):
        nums = self.nums
        target = self.target
        dict = defaultdict(int)
        indexs = []

        for i,n in enumerate(nums):
            if n in dict and i != dict[n]:
               indexs.extend([i, dict[n]])
            else:
                dict[target - n] = i
        return indexs        


s = Solution()
print(s.twoSum())
