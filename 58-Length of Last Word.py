class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        i = len(s)-1

        while i>=0:
            if s[i]==" " and count==0:
                pass
            elif s[i]==" ":
                break
            else:
                count+=1
            i-=1
        return count


################## Another method
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])