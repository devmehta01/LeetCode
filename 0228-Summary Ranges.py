class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        start = current = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == current+1:
                current += 1
            else:
                if start != current:
                    ans.append(str(start)+"->"+str(current))
                    start = current = nums[i]
                else:
                    ans.append(str(start))
                    start = current = nums[i]
        if start == current:
            ans.append(str(start))
        else:
            ans.append(str(start)+"->"+str(current))
        return ans