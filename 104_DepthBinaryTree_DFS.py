# Definition for a binary tree node.
# class TreeNode(object):
# def __init__(self, x):
# self.val = x
# self.left = None
# self.right = None
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root is None):
            return 0
        lmax = self.maxDepth(root.left)+1
        rmax = self.maxDepth(root.right)+1
        return lmax if lmax>rmax else rmax
