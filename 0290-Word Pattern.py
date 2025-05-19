class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        char_2_word = {}
        word_2_char = {}

        for i in range(len(pattern)):
            if pattern[i] not in char_2_word:
                if s[i] not in word_2_char:
                    char_2_word[pattern[i]] = s[i]
                    word_2_char[s[i]] = pattern[i]
                else:
                    return False
            else:
                if s[i] not in word_2_char:
                    return False
                else:
                    if char_2_word[pattern[i]] != s[i] or word_2_char[s[i]] != pattern[i]:
                        return False
        return True