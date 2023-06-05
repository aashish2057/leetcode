from collections import defaultdict


class Frequent:
    def __init__(self) -> None:
        self.nums = [3,0,1,0]
        self.k = 1 
        seff.y = 0
    def topKFrequent(self):
        frequency = defaultdict(int)

        for num in self.nums:
            frequency[num] += 1

        occurances = [[] for _ in range(len(self.nums))] 
        for key, value in frequency.items():
            occurances[value-1].append(key)
            print(key, value)
        res = []
        for occur in reversed(occurances):
            if self.k == 0:
                break
            if len(occur) > 0:
                for num in occur:
                    if self.k == 0:
                        break
                    res.append(num)
                    self.k -= 1

        return res
f = Frequent()
print(f.topKFrequent())
