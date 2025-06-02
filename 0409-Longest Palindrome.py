class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashtable = {}
        for char in s:
            hashtable[char] = 1 + hashtable.get(char, 0)
        
        total = 0
        odd_exists = 0

        for key in hashtable:
            if hashtable[key] % 2 == 0:
                total += hashtable[key]
            else:
                odd_exists = 1
                total += hashtable[key] - 1
        
        if odd_exists:
            total += 1
        
        return total