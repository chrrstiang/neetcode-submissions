# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def findDepth(node, depth):
            if node == None:
                return depth
            depth += 1
            left = findDepth(node.left, depth)
            right = findDepth(node.right, depth)
            return max(left, right)
        return findDepth(root, 0)