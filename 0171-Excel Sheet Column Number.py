class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        ans = 0
        for char in columnTitle:
            ans = ans * 26 + (ord(char)-64)
        return ans