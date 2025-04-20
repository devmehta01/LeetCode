class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return 1
        prevstep = 1
        prev2step = 0

        for _ in range(n):
            current = prevstep + prev2step
            prev2step = prevstep
            prevstep = current
        return prevstep