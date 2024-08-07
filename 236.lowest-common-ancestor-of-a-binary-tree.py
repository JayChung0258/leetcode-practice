#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.p_path = []
        self.q_path = []
        self.path = []

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # find two paths of p and q, and get the last same node (lowest ancestor)
        self.traversal(root, p, q)

        res = root

        for i in range(min(len(self.p_path), len(self.q_path))):
            if self.p_path[i] == self.q_path[i]:
                res = self.p_path[i]

        return res


    def traversal(self, root, p, q):
        # traversal
        if not root:
            return
        
        self.path.append(root)

        if root.val == p.val:
            self.p_path = self.path[:]

        if root.val == q.val:
            self.q_path = self.path[:]

        self.traversal(root.left, p, q)
        self.traversal(root.right, p, q)
        
        self.path.pop()



# @lc code=end

