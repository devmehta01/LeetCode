class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        smaller, larger = (nums1,nums2) if len(nums1) <= len(nums2) else (nums2,nums1)
        set1 = set(smaller)

        set2 = set()

        for num in larger:
            if num in set1:
                set2.add(num)
            if len(set2) == len(set1):
                break
        return list(set2)