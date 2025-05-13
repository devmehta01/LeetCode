class Solution:
    def isHappy(self, n: int) -> bool:
        my_set = set()
        sum_num = 0
        while True:
            while n:
                last_num = n%10
                n = n//10
                sq = last_num**2
                sum_num += sq
            if sum_num == 1:
                return True
            else:
                if sum_num in my_set:
                    return False
                my_set.add(sum_num)
                n = sum_num
                sum_num=0