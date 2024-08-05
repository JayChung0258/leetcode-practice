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
        
        # at least len(citations) paper >= 0 cite
        # at least len(citations) - only 0 times paper -> at least >= 1 citation paper

        freq = [0] * 1001
        ct = Counter(citations)

        for key, value in ct.items():
            freq[key] = value


        least_times = len(citations)

        for i in range(len(freq)):
            # print(i, least_times)
            if least_times < i:
                return i-1

            least_times -= freq[i]
            
            


# @lc code=end

