# Time Complexity - O(n) as the loop runs only once in the base case -> O(n+n) 
# Space Complexity - O(n) as hash map max 9 digits but call stack of height of tree -> O(n + 1).


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        freq = {}
        def dfs(node):
            nonlocal freq
            freq[node.val] = freq.get(node.val, 0) + 1
            if not node.left and not node.right:
                c = 0
                for f in freq.values():
                    if f%2!=0:
                        c += 1
                
                freq[node.val] = freq.get(node.val, 0) - 1
                return 1 if c<=1 else 0

            res = 0
            if node.left:
                res += dfs(node.left)
            if node.right:
                res += dfs(node.right)

            freq[node.val] = freq.get(node.val, 0) - 1
            return res

        return dfs(root)