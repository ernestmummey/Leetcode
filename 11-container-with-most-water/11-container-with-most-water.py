class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0 # We don't have to worry about negatives
        while l < r:
            current_sum = (r - l) * min(height[l], height[r])
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            max_area = max(max_area, current_sum)
        return max_area
            