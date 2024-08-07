#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

import random
# @lc code=start
class RandomizedSet:
    # key is how to implement remove
    # random must use list or otherwise cannot be O(1)

    def __init__(self):
        self.li = []
        self.v_to_idx = {}

    def insert(self, val: int) -> bool:
        if val in self.v_to_idx:
            return False
        
        self.v_to_idx[val] = len(self.li)
        self.li.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.v_to_idx:
            return False
        # swap
        idx = self.v_to_idx[val]
        self.v_to_idx[self.li[-1]] = idx
        self.li[idx], self.li[-1] = self.li[-1], self.li[idx]
        
        self.li.pop()
        del self.v_to_idx[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.li)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

