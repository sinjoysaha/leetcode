# Recursion
# Time Complexity - O(n)
# Space Complexity - O(2^n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def bst(root):
            nonlocal res
            if (not root):
                return
            if (root.val < low):
                bst(root.right)
            elif (root.val > high):
                bst(root.left)
            else:
                res = res + root.val
                bst(root.left)
                bst(root.right)

        bst(root)
        return res