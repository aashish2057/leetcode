class Solution:
    def __init__(self):
        self.nums = [5,1,2,3,4]

    def findMin(self):
        nums = self.nums
        left, right = 0, len(nums) - 1
        minimum = float("inf")
        while left <= right:
            mid = (left + right) // 2
            
            minimum = min(nums[mid], minimum)
            
            if nums[left] > nums[mid]:
                right = mid - 1
            
            if nums[right] < nums[mid]:
                left = mid + 1

        return minimum


s = Solution()
print(s.findMin())
