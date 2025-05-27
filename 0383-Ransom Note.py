class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        mapping = {}
        for char in ransomNote:
            mapping[char] = 1 + mapping.get(char, 0)
        
        for char in magazine:
            if char in mapping:
                mapping[char] -= 1
                if mapping[char] == 0:
                    del mapping[char]
                    if len(mapping) == 0:
                        return True
        
        return False