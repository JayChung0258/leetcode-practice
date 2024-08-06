#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort
        res = []
        dt = defaultdict(list)
        for _str in strs:
            key = str(sorted(_str))
            dt[key].append(_str)

        return dt.values()




        
# @lc code=end

