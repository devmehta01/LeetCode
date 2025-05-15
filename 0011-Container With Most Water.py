class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0

        while left < right:
            ans = max(ans, (right-left) * min(height[left], height[right]))
            if height[left] < height[right]:
                prev_left = height[left]
                left += 1
                while prev_left >= height[left] and left < right:
                    left += 1
            else:
                prev_right = height[right]
                right -= 1
                while prev_right >= height[right] and left < right:
                    right -= 1 
        return ans