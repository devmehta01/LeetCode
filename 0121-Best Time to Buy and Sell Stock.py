class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_so_far = 0
        min_val = prices[0]
        for price in prices:
            if price < min_val:
                min_val = price
            else:
                max_so_far = max(max_so_far, price - min_val)
        return max_so_far