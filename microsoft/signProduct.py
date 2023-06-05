class Solution:
    def __init__(self):
        self.nums = [1,-2,-3,-4,3,2,1]

    def arraySign(self):
        nums = self.nums
        product = 1
        for n in nums:
            product *= n
        
        return self.signFunc(product)

    def signFunc(self, num: int) -> int:
        if num == 0:
            return 0
        elif num < 0:
            return -1
        else:
            return 1
            
s = Solution()
print(s.arraySign())
