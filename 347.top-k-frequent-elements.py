#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
import heapq
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # max heap

        ct = Counter(nums)

        max_heap = []
        for key, value in ct.items():
            heapq.heappush(max_heap, (-value, key))

        res = []
        for _ in range(k):
            value, key = heapq.heappop(max_heap)
            res.append(key)

        return res



        
            
# @lc code=end

