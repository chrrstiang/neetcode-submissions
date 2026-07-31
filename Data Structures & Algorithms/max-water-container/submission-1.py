class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        left, right = 0 , len(heights) - 1

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            print(area, left, right)
            if area > maxArea:
                maxArea = area
            
            if heights[right] < heights[left]:
                curr = right - 1
                while heights[curr] < heights[right]:
                    curr -= 1
                right = curr
            else:
                curr = left + 1
                while heights[curr] < heights[left]:
                    curr += 1
                left = curr
        
        return maxArea