class Solution:
    def __init__(self):
        self.height = [1,2,3,4,5,6]

    def maxArea(self):
        height = self.height
        left, right = 0, len(height) - 1
        area = 0

        while left <= right:
            area = max(area, min(height[left], height[right]) * (right - left))
             
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return area



s = Solution()
print(s.maxArea())
