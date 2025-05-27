class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        k = n // m
        divisible_sum = m * k * (k + 1) // 2
        return total - 2 * divisible_sum


### ANOTHER METHOD
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num2 = 0
        multiple = 0
        while multiple + m <= n:
            multiple += m
            num2 += multiple
        range_sum = (n*(n+1)) // 2
        num1 = range_sum - num2
        return num1 - num2