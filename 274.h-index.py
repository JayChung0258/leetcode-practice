#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        res = 0
        for i in range(len(citations)):
            if citations[i] >= i+1:
                res = i+1


        return res

# @lc code=end

