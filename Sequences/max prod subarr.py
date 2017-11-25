# https://leetcode.com/problems/maximum-product-subarray/description/

#get max product from right to left, then left to right
#compare lTor and rTol and return max
#if max_prod =0, then change to 1
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr_len = len(nums)
        right_to_left = left_to_right = nums[0]
        
        max_prod = 1
        
        #from left to right
        for i in range(arr_len):
            max_prod = max_prod * nums[i]
            
            if max_prod > left_to_right:
                left_to_right = max_prod

            if max_prod == 0: max_prod = 1
        
        max_prod = 1
        
        #from right to left
        for i in range(arr_len-1, -1, -1):
            max_prod = max_prod * nums[i]
            
            if max_prod > right_to_left:
                right_to_left = max_prod

            if max_prod == 0: max_prod = 1
        
        return max(right_to_left, left_to_right)