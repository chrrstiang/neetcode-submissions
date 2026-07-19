class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            min_height = min(heights[left], heights[right])
            area = min_height * (right - left)
            max_area = max(area, max_area)
            if heights[left] == min_height:
                while left < right and heights[left] <= min_height:
                    left += 1
            else:
                while left < right and heights[right] <= min_height:
                    right -= 1
            
        return max_area