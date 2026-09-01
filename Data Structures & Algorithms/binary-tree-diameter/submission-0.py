# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def findDiam(node):
            if node == None:
                return 0
            left = findDiam(node.left)
            right = findDiam(node.right)
            diam = left + right
            nonlocal max_diameter 
            max_diameter = max(diam, max_diameter)
            return max(left, right) + 1
        findDiam(root)
        return max_diameter