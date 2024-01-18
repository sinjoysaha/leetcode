# Time Complexity - O(n)
# Space Complexity - O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b, c = 1, 1, 1
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c

        return c