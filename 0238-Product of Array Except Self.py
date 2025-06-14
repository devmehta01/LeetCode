class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        left_prod = 1
        for i in range(len(nums)):
            answer[i] *= left_prod
            left_prod *= nums[i]
        
        right_prod = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= right_prod
            right_prod *= nums[i]
        
        return answer