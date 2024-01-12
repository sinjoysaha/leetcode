# Time Complexity -> O(n)
# Space Complexity -> O(1)

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        t = 0
        v = set(['a','e','i','o','u','A','E','I','O','U'])
        for i in range(len(s)//2):
            t += (s[i] in v) - (s[len(s)-i-1] in v)

        return not t