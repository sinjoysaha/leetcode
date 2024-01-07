# DP

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        t = [{} for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                t[i][diff] = t[i].get(diff, 0) + t[j].get(diff, 0) + 1
                res += t[j].get(diff, 0) + 1

        return res - ((len(nums)*(len(nums)-1)) // 2)