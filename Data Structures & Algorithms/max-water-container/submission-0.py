class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # have a left and right pointer
        # Calculate area
        # Move smaller bar pointer until taller bar is found
        # Continue until left and right pointer don't cross each other


        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            area = min(left_height, right_height) * (right - left)
            if area > max_area:
                max_area = area
            if left_height < right_height:
                while left < right and heights[left] <= left_height:
                    left += 1
            else:
                while left < right and heights[right] <= right_height:
                    right -= 1
        return max_area
            


