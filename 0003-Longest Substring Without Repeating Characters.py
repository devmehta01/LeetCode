class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = ""
        max_so_far = i = 0
        while i < len(s):
            if s[i] in ans:
                ans = ans[1:]
            else:
                ans+=s[i]
                if max_so_far < len(ans):
                    max_so_far = len(ans)
                i+=1
        return max_so_far