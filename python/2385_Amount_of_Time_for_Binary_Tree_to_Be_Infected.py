# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Try to build separate graph

import collections

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        start_node = None
        def dfs(root):
            nonlocal start_node
            if root is None:
                return
            if root.val==start:
                start_node = root
            if root.left:
                root.left.parent = root
                dfs(root.left)
            if root.right:
                root.right.parent = root
                dfs(root.right)

        root.parent = None
        dfs(root)
        dq = collections.deque()
        dq.append((start_node, 0))
        visited = {}
        visited[start_node] = 0
        while dq:
            curr, dist = dq.popleft()
            for n in [curr.left, curr.right, curr.parent]:
                if n is not None and n not in visited:
                    visited[n] = dist+1
                    dq.append((n, dist+1))

        return max(visited.values())
