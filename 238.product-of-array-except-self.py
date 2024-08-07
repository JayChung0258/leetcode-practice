#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # prefix and suffix or precomputing

        prefix = []
        acc = 1
        for i in range(len(nums)):
            acc *= nums[i]
            prefix.append(acc)

        suffix = []
        acc = 1
        for i in range(len(nums)-1, -1, -1):
            acc *= nums[i]
            suffix.append(acc)

        suffix.reverse()

        res = [0]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                res[i] = suffix[i+1]

            elif i == len(nums)-1:
                res[i] = prefix[-2]
            else:
                res[i] = prefix[i-1] * suffix[i+1]

        return res

        
# @lc code=end

