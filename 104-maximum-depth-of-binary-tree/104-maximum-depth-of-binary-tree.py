# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.countDepth(root, 0)
    
    def countDepth(self, root, count):
        if(root==None):
            return count
        leftCount = self.countDepth(root.left, count+1)
        rightCount = self.countDepth(root.right, count+1)
        return max([leftCount, rightCount])