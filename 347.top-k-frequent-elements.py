#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort

        # bucket key(freq): value[number]

        ct = Counter(nums)
        
        # put into bucket
        bucket = [[] for _ in range(len(nums)+1)]
        for key, freq in ct.items():
            bucket[freq].append(key)

        # find top k freq
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

            
# @lc code=end

