# Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree.
# Find all the keys of tree in range k1 to k2.
# i.e. print all x such that k1<=x<=k2 and x is a key of given BST.
# Return all the keys in ascending order.
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """
    def searchRange(self, root, k1, k2):
        res = []
        self.dfs(root, k1, k2, res)
        return res

    def dfs(self, root, k1, k2, res):
        if root is None:
            return

        if root.val < k1:
            self.dfs(root.right, k1, k2, res)
        elif root.val > k2:
            self.dfs(root.left, k1, k2, res)
        else:
            self.dfs(root.left, k1, k2, res)
            res.append(root.val)
            self.dfs(root.right, k1, k2, res)