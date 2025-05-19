class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)+1
        expected_sum = (length*(length-1))/2
        actual_sum = sum(nums)
        return int(expected_sum-actual_sum)