# https://leetcode.com/problems/contains-duplicate/

from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq_dict = defaultdict(int)
        # go over the list
        # add counter dictionary for each int
        # check if value is more than  1 and return true if true
        
        for elem in nums:
            freq_dict[elem] += 1
            if freq_dict[elem] == 2:
                return True
        return False
        