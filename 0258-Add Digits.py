class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        sum_num = 0
        while num:
            sum_num += num%10
            num//=10
        return self.addDigits(sum_num)