#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

import random
# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}
        self.li = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        
        self.li.append(val)
        self.val_to_index[val] = len(self.li)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        
        # swap value and index
        idx = self.val_to_index[val]
        self.val_to_index[self.li[-1]] = idx
        self.li[idx], self.li[-1] = self.li[-1], self.li[idx]

        self.li.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        res = random.choice(self.li)
        return res


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

