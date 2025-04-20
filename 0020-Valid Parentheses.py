class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {')':'(', '}':'{', ']':'['}
        ans = ""

        for char in s:
            if char in mapping:
                if len(ans)!=0 and mapping[char] == ans[-1]:
                    ans = ans[:-1]
                else:
                    return False
            else:
                ans += char
        return len(ans)==0