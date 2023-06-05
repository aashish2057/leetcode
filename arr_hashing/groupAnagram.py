from collections import defaultdict


class Anagram:
    def __init__(self) -> None:
        self.strs = ["eat","tea","tan","ate","nat","bat"]
    def groupAnagrams(self):
        res = []
        anagrams = defaultdict(list)

        for string in self.strs:
            chars = [0] * 26
            for c in string:
                chars[ord(c)-ord('a')] += 1
            anagrams[tuple(chars)].append(string)
        
        for key, value in anagrams.items():
            res.append(value)
        print(res)
a = Anagram()
a.groupAnagrams()
