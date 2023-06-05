class Polish:
    def __init__(self) -> None:
        self.tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

    def evalRPN(self):
        stack = []

        for c in self.tokens:
            if c in "*/+-":
                right, left = stack.pop(), stack.pop()
                if c == "+":
                    stack.append(left + right)
                if c == "-":
                    stack.append(left - right)
                if c == "*":
                    stack.append(left * right)
                if c == "/":
                    stack.append(int(left / right))
            else:
                stack.append(int(c))
            print(stack)
        return stack[-1]
p = Polish()
print(p.evalRPN())


