# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # check for mid
        # check if left/right side is ascending
        # update value if value is between ascending range

        lo = 0
        hi = len(nums) -1
        
        while(lo<=hi):
            mid = int((lo+hi)/2)
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[hi]:
                if target> nums[mid] and target <= nums[hi]:
                    lo =  mid + 1
                else:
                    hi = mid - 1
            elif nums[lo] <=   nums[mid]:
                if target >= nums[lo] and target < nums[mid]:
                    hi = mid -1
                else:
                    lo = mid +1
        return -1