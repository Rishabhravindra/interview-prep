# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # check for array with size 1
        # loop through array and if next index value is more than curr index value, then return next value
        # if nothing is returned by now, that means there was not rotation, and hence nums[0] is the smallest element
        
        if len(nums) == 1:
            return nums[0]
        
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]