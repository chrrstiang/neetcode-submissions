# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        balance = True
        
        def getHeight(node):
            if node == None:
                return 0
            left = getHeight(node.left)
            right = getHeight(node.right)
            nonlocal balance
            if abs(left - right) >= 2:
                balance = False
            return max(left, right) + 1
        getHeight(root)
        return balance
