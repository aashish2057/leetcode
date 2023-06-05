class Sum:
    def __init__(self) -> None:
        self.numbers = [-1, 0]
        self.target = -1 

    def twoSum(self):
        left, right = 0, len(self.numbers) - 1
        res = []
        while left < right: 
            total = self.numbers[left] + self.numbers[right]
            
            if total == self.target:
                res.append(left+1)
                res.append(right+1)
                break
            if total > self.target:
                right -= 1
            if total < self.target:
                left += 1
        return res

s = Sum()
print(s.twoSum())

