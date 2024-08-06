#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # Greedy

        farthest = 0

        for i in range(len(nums)):
            farthest = max(farthest, i+nums[i])

            if i >= farthest:
                break

        return farthest >= len(nums)-1


# @lc code=end
