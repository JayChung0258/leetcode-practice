#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        farthest = 0
        bound = 0
        step = 0
        for i in range(len(nums)-1):
            farthest = max(i+nums[i], farthest)

            if i == bound:
                step += 1
                bound = farthest

        return step
        

        
# @lc code=end

