class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        smaller, larger = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)

        counts = {}

        for num in smaller:
            counts[num] = 1 + counts.get(num, 0)
        
        ans = []
        
        for num in larger:
            if num in counts:
                counts[num] -= 1
                ans.append(num)
                if counts[num] == 0:
                    del counts[num]
                    if not counts:
                        break
        return ans