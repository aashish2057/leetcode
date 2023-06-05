class Solution:
    def __init__(self):
        self.arr = [, 10, 3, 2, 1, 0]

    def peakOfMountain(self):
        arr = self.arr

        left, right = 0, len(arr) - 1
        peak = 0
        while left <= right:
            mid = (left + right) // 2


            if arr[mid-1] <= arr[mid] and arr[mid+1] <= arr[mid]:
                peak = mid
                break

            if arr[mid-1] > arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return peak

s = Solution()
print(s.peakOfMountain())
