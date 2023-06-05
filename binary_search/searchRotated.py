class Solution:
    def __init__(self):
        self.nums = [4,5,6,7,8,1,2,3]
        self.target = 8  
    def search(self):
        nums = self.nums
        target = self.target

        left, right = 0, len(nums) - 1

        index = -1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                index = mid
                break
            
            if nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return index

s = Solution()
print(s.search())
