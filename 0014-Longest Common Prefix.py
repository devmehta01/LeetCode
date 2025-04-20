class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        smallest_len = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i]) < smallest_len:
                smallest_len = len(strs[i])

        ans = ""

        for i in range(smallest_len):
            char = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != char:
                    return ans
            ans += char
        return ans