class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        curr = len(digits)-1

        digits[curr] = digits[curr]+1
        carry = digits[curr]//10

        if carry:
            while carry!=0:
                digits[curr] = digits[curr] % 10
                if curr == 0:
                    digits.insert(0,carry)
                    return digits
                else:
                    curr -=1
                    digits[curr]+=carry
                    carry = digits[curr]//10
        
        return digits