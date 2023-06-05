class Parentheses:
    def __init__(self) -> None:
        self.s = "(((((())))))"

    def isValid(self) -> bool:
        stack = []
        braces = {")":"(", "]":"[", "}":"{"}
        valid = True
        for c in self.s:
            if c in braces.values():
                stack.append(c)

            if c in braces:
                if stack and stack[-1] == braces[c]:
                    stack.pop()
                else:
                    return False 
        valid = len(stack) == 0
        return valid

p = Parentheses()
print(p.isValid())
