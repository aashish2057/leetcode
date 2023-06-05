class TwoBalls:
    def __init__(self) -> None:
       self.heights = [0,0,0,0,0,0,0,1,1,1,1,1,1]
    def height(self) -> int:
        left, right = 0, len(self.heights)
        minHeight = right
        while left < right:
            mid = (left + right) // 2 
            if self.heights[mid] == 1:
                minHeight = min(minHeight, mid)
                right = mid - 1
            if self.heights[mid] == 0:
                left = mid + 1
        return minHeight

two = TwoBalls()
print(two.height())
          

