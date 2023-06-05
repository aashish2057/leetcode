import math
class Solution:
    def __init__(self):
        self.piles = [312884470]
        self.h = 312884469 

    def minEatingSpeed(self):
        biggestPile = max(self.piles)
        left, right = 1, biggestPile
        k = biggestPile
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in self.piles:
                hours += math.ceil(pile / mid)
            if hours <= self.h:
                k = min(k, mid)
                right = mid - 1
            else:
                left = mid + 1
        return k


s = Solution()
print(s.minEatingSpeed())
