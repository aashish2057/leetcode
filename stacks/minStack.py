class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.minStack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = val 
        if self.minStack:
            minVal = min(val, self.minStack[-1])
        self.minStack.append(minVal)
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minStack[-1]

s = Stack()
print(s.push(-2))
print(s.push(0))
print(s.push(-3))
print(s.getMin())
print(s.pop())
print(s.top())
print(s.getMin())
