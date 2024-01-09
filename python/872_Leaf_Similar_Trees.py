# Time Complexity - O(n), number of leaves
# Space Complexity - O(n), number of leaves (due to recursive call stack)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seqs = [[], []]
        def dfs(root, i):
            nonlocal seqs
            if not root:
                return 
            if not root.left and not root.right:
                seqs[i].append(root.val)
                return
            dfs(root.left, i)
            dfs(root.right, i)

        dfs(root1, 0)
        dfs(root2, 1)
        return seqs[0]==seqs[1]