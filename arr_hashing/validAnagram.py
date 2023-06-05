from collections import defaultdict


class Anagram:
    def __init__(self) -> None:
        self.s = "anagram"
        self.t = "nagaram"

    def isAnagram(self) -> bool:
        sCharacters = defaultdict(int)
                              
        for indx in range(len(self.s)):
            sCharacters[self.s[indx]] += 1
            
        for char in self.t:
            sCharacters[char] -= 1

        for key in sCharacters:
            if sCharacters[key] != 0:
                return False
        return True



a = Anagram()
print(a.isAnagram())
