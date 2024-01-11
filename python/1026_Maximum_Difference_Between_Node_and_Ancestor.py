# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. Time -> O(n), Space -> O(n) -Traverse Top Down and store node, list of ancestors in dict. Find Max Diff.

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ancestorOf = {}
        def dfs(root):
            nonlocal ancestorOf
            if root is None:
                return 
            if root.left:
                if root.val in ancestorOf:
                    ancestorOf[root.left.val] = ancestorOf[root.val] + [root.val]
                else:
                    ancestorOf[root.left.val] = [root.val]
                dfs(root.left)
            if root.right:
                if root.val in ancestorOf:
                    ancestorOf[root.right.val] = ancestorOf[root.val] + [root.val]
                else:
                    ancestorOf[root.right.val] = [root.val]
                dfs(root.right)
        
        dfs(root)
        max_diff = 0
        for n, l in ancestorOf.items():
            for i in l:
                max_diff = max(max_diff, abs(n-i))

        return max_diff       

# 2. Optimized - Time -> O(n), Space -> O(n) - Top Down, find max, min for every path till leaf and return Max Diff.
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, maxn, minn):
            if root is None:
                return 
            max_diff_l, max_diff_r = 0, 0
            if root.left:
                max_diff_l = dfs(root.left, max(maxn, root.left.val), min(minn, root.left.val))
            if root.right:
                max_diff_r = dfs(root.right, max(maxn, root.right.val), min(minn, root.right.val))
            return max(max_diff_l, max_diff_r, (maxn-minn))
        
        return dfs(root, root.val, root.val)       