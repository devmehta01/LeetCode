class Solution:
    def reverse(self, x: int) -> int:
        multiplier = 1
        ans = 0

        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            ans = ans*10 + (x % 10)
            x //= 10

        ans *= sign

        if ans < -2**31 or ans > 2**31 - 1:
            return 0

        return ans