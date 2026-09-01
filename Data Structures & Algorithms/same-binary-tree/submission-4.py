# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            if p == q:
                return True
            elif p == None or q == None:
                return False
            left = check(p.left, q.left)
            right = check(p.right, q.right)
            return p.val == q.val and left and right
        return check(p, q)