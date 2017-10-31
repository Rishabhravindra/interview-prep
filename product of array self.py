# https://leetcode.com/problems/product-of-array-except-self/discuss/

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):

        # loop from 0
            # attack from right
            # append 
        # loop from n-1
            # attack from left
            # append
    p = 1
    arr_len = len(nums)
    
    output = []
    i = 0
    for i in xrange(arr_len):
        output.append(p)
        p = p * nums[i]
    
    p = 1
    for i in range(arr_len-1, -1, -1):
        output[i] = output[i] * p
        p = p *nums[i]
    return output
        
        
    
        