# https://leetcode.com/problems/maximum-subarray/discuss/

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # assign current sum and max sum as the first element
        # loop through the list and compare the current element with the sum of current element and prev largest sum
        # compare maximum sum stored with the new one generated
        # return maximum sum in the end
        
        curr_sum = nums[0]
        max_sum = nums[0]
        
        for elem in nums[1:]:
            curr_sum = max(elem, elem+curr_sum)
            max_sum  = max(max_sum, curr_sum)
        return max_sum