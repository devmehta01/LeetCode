class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s = {}
        hash_t = {}

        for x,y in zip(s,t):
            hash_s[x] = 1 + hash_s.get(x, 0)
            hash_t[y] = 1 + hash_t.get(y, 0)

        return hash_s == hash_t


######## ANOTHER METHOD
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)