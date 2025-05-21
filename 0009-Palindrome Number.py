class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]


######### ANOTHER METHOD
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10 == 0 and x!=0):
            return False
        rev = 0

        while rev < x:
            rev = rev*10 + x%10
            x //= 10
        return rev == x or x == rev//10