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
        ct = Counter(citations)
        freq = [0] * 1001

        for key, value in ct.items():
            freq[key] = value


        least_times = len(citations)
        for i in range(len(freq)):

            if least_times < i:
                return i - 1

            least_times -= freq[i]


# @lc code=end

