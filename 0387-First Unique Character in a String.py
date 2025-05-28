class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for i in range(len(s)):
            if s[i] in counts:
                counts[s[i]] = -1
            else:
                counts[s[i]] = i
        idx = len(s)
        for char in counts:
            if counts[char] != -1:
                if counts[char] < idx:
                    idx = counts[char]
        if idx == len(s):
            return -1
        else:
            return idx