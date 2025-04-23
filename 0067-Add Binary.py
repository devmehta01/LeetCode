class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        idxa = len(a)-1
        idxb = len(b)-1

        carry = 0

        ans = ""

        while idxa>=0 or idxb>=0 or carry==1:
            if idxa>=0:
                carry += int(a[idxa])
                idxa -=1
            if idxb>=0:
                carry += int(b[idxb])
                idxb -=1
            ans = str(carry%2) + ans
            carry = carry//2

        return ans 