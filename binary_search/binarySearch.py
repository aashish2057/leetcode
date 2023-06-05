class BinarySearch:
    def __init__(self) -> None:
        self.nums = [5]
        self.target = 5

    def search(self) -> int:
        left, right = 0, len(self.nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) //2
            print(mid) 
            if self.nums[mid] == self.target:
                index = mid
                break
            elif self.nums[mid] > self.target:
                right = mid - 1
            else:
                left = mid + 1
        return index
            

b = BinarySearch()
print(b.search())
