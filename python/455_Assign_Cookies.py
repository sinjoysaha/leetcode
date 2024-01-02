# Greedy approach -> sort both arrays
# Time Complexity - O(n)

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j, m = 0, 0, 0
        while j < len(s) and i < len(g):
            if g[i]<=s[j]:
                i+=1
                m+=1
            j+=1

        return m