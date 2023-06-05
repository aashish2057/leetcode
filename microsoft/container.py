class Solution:
    def __init__(self):
        self.heights = [1,1]

    def maxArea(self):
        heights = self.heights
        
        mArea = float("-inf")

        left, right = 0, len(heights) - 1

        while left < right: 
            area = min(heights[left], heights[right]) * (right - left)

            mArea = max(mArea, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return mArea

s = Solution()
print(s.maxArea())
