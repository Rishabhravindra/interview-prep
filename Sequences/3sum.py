class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # have three nums i,j,k 
        # sort the list
        # start j = i + 1
        # start k = len - 1
        # if i + j + k > 0, lower k to k--
        # if i + j + k < 0, increase j to j++
        
        # prepare sorted unqiue list
        nums.sort()
        sol_set = []
        for i in range(len(nums)-2):
            j = i+1
            
            if nums[i] + nums[j] + nums[j+1] > 0:
                return sol_set
            
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            k = len(nums) - 1
            while j < k:
                if j> i+1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                target = nums[i] + nums[j] + nums[k]                    
                
                if target > 0:
                    k -= 1                    
                else:
                    if target == 0:
                        res = [nums[i], nums[j], nums[k]]
                        sol_set.append(res)
                    j += 1   
        return sol_set