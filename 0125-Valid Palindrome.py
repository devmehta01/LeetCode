class Solution(object):
    import re
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join(re.findall("[a-zA-Z0-9]+", s)).lower()
        return s==s[::-1]