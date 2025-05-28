class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = {}
        for char in s:
            counts[char] = 1 + counts.get(char, 0)
        
        for char in t:
            if char not in counts:
                return char
            else:
                counts[char] -= 1
                if counts[char] == 0:
                    del counts[char]