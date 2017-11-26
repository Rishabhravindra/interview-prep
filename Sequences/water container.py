# https://www.programcreek.com/wp-content/uploads/2014/03/container-with-most-water-400x161.png
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0 
        
        while left < right:
            curr_area =  min(height[left], height[right]) * (right - left)
            max_area = max(max_area, curr_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area                