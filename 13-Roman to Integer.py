class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sum_val = prev = 0

        for char in s:
            current = mapping[char]
            sum_val += current if current <= prev else (current - 2*prev)
            prev = current
        return sum_val