class Temperature:
    def __init__(self) -> None:
        self.temperatures = [73,74,75,71,69,72,76,73]

    def dailyTemperatures(self):
        answer = [0] * len(self.temperatures)
        stack = []

        for index, temp in enumerate(self.temperatures):
            while stack and temp > stack[-1][0]:
                answer[stack[-1][1]] = index - stack[-1][1]
                stack.pop()
            stack.append((temp, index))
            print(stack, answer)
        return answer
t = Temperature()
t.dailyTemperatures()
