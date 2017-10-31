# run time O(n)
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement = {}
        i = 0
        for elem in nums:
            comp = target - elem
            if comp in complement:
                return [complement[comp],i]
            complement[elem] = i
            i += 1