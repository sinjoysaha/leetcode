# 1. Traversing in reverse order and using a list for 1D DP
# Time Complexity - O(n)
# Space Complexity - O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1)
        dp[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])

        return dp[0]

# 2. Still traversing in reverse order and using two extra variables (because at any i you only look at atmost i+2)
# Time Complexity - O(n)
# Space Complexity - O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_0, dp_1, dp_2 = nums[-1], nums[-1], 0
        for i in range(len(nums)-2, -1, -1):
            dp_0 = max(nums[i] + dp_2, dp_1)
            dp_2 = dp_1
            dp_1 = dp_0

        return dp_0

# 3. Traversing in order and using only one extra variables.
# Time Complexity - O(n)
# Space Complexity - O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_0, dp_1 = nums[0], 0
        for i in range(1, len(nums)):
            dp_0, dp_1 = max(nums[i] + dp_1, dp_0), dp_0

        return dp_0

