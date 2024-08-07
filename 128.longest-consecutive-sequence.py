#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
from typing import List
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # the key is to find the starter
        # starter: no (val-1) element exist -> a potenial starter
        nums = set(nums)
        res = 0
        for num in nums:
            if num-1 not in nums:
                lng = 0
                n = num
                while n in nums:
                     lng += 1
                     n += 1

                res = max(res, lng)
        return res





# @lc code=end

