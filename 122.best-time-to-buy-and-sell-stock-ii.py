#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # 2 ptrs + Greedy
        # if next price is lower than now, make profit once

        prices.append(0)
        
        res = 0
        low = prices[0]
        for i in range(len(prices)-1):
            if prices[i+1] < prices[i]:
                # cal profit
                res += prices[i]-low
                low = prices[i+1]

        return res




# @lc code=end

