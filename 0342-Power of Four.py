class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <=0:
            return False
        while n%4 == 0:
            n //=4
        return n==1


######## ANOTHER METHOD
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
            
        return math.log(n, 4).is_integer()