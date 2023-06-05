from typing import DefaultDict


class TwoSum:
    def __init__(self) -> None:
      self.nums = [3,2,4]
      self.target = 6 
    def twoSum(self) -> list[int]:
        difference = DefaultDict(int)

        for indx, value in enumerate(self.nums):
            if value in difference:
                return [indx, difference[value]]
            difference[self.target - value] = indx
        return []
two = TwoSum()
print(two.twoSum())

