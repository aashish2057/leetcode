class Palindrome:
    def __init__(self) -> None:
        self.s = "race a car"

    def validPalindrome(self) -> bool:
        self.s = self.s.replace(" ", "")
        self.s = self.s.lower()
        self.s = ''.join(c for c in self.s if c.isalnum())
        valid = True
        left, right = 0, len(self.s) - 1

        while left < right:
            if self.s[left] != self.s[right]:
                valid = False
                break
            left += 1
            right -= 1
        return valid
p = Palindrome()
print(p.validPalindrome())
