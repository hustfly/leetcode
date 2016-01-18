tion for a binary tree node.
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
        nodes =[]
        dept=0
        count=1 #the nodes of every level
        nodes.append(root)
        while(len(nodes)>0):
            p = nodes[0]
            del(nodes[0])
            count = count-1
            if(p.left is not None):
                nodes.append(p.left)
            if(p.right is not None):
                nodes.append(p.right)
            if(count==0):
                count=len(nodes) #important!
                dept=dept+1 #important!          
        return dept
