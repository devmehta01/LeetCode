class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i=0
        while i <= len(nums)-3:
            j = i+1
            k = len(nums)-1
            
            while j<k:
                sum_val = nums[i] + nums[j] + nums[k]
                if sum_val == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    while k > j and nums[k] == nums[k-1]:
                        k -= 1
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                    k -= 1
                elif sum_val > 0:
                    while k > j and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                else:
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1

            i += 1
            while i <= len(nums)-3 and nums[i] == nums[i-1]:
                i += 1
        
        return ans