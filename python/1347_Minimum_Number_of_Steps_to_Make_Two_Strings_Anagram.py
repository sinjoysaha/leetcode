# Time Complexity - O(n)
# Space Complexity - O(n)

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
            d[t[i]] = d.get(t[i], 0) - 1

        s = 0
        for v in d.values():
            s += abs(v)

        return s//2