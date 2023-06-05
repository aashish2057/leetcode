class Stock:
    def __init__(self) -> None:
        self.prices = [4,3,2,1]

    def maxProfit(self):
        profit = 0

        left, right = 0, 0

        while right < len(self.prices):
            if self.prices[right] > self.prices[left]:
                profit = max(profit, self.prices[right] - self.prices[left])
            else:
                left = right
            right += 1
        return profit

s = Stock()
print(s.maxProfit())
