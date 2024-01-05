# DP

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        t = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i] and t[i] <= t[j]:
                    t[i] = t[j] + 1

        return max(t)
