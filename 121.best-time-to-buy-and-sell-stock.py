#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 ptrs + Greedy
        profit = 0

        low = prices[0]

        for i in range(len(prices)):
            
            if low > prices[i]:
                low = prices[i]


            profit = max(profit, prices[i]-low)


        return profit

        
# @lc code=end

