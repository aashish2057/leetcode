import math
class Sorting:
    def __init__(self):
       self.s = "hello" 
    def insertionSort(self, nums):
        for index, value in enumerate(nums):
            curr = index
            while curr > 0 and nums[curr] < nums[curr-1]:
                nums[curr], nums[curr-1] = nums[curr-1], nums[curr]
                curr -= 1
        return nums

    def selectionSort(self, nums):
        minimum = [(math.inf), 0] 
        for index, value in enumerate(nums):
            curr = index
            while curr < len(nums):
                if nums[curr] < minimum[0]:
                    minimum = [nums[curr], curr]
                curr += 1
            nums[index] = minimum[0]
            nums[minimum[1]] = value
            minimum = [(math.inf), 0]
        return nums

    def bubbleSort(self, nums):
        swap = False

        while not swap:
            index = 0
            swapCount = 0 
            while index + 1 < len(nums):
                if nums[index] > nums[index+1]: 
                    tmp = nums[index]
                    nums[index], nums[index+1] = nums[index+1], tmp 
                    swapCount += 1
                index += 1

            if swapCount == 0:
                swap = True
        return nums

s = Sorting()
nums = [5,3,1,2,4]
print("Insertion Sorting, O(n^2)")
print(s.insertionSort(nums))

nums = [5,6,1,2,7,8,3]
print("Selection Sorting, O(n^2)")
print(s.selectionSort(nums))

nums = [5,6,1,2,7,8,3]
print("Bubble Sorting, O(n^2)")
print(s.bubbleSort(nums))
