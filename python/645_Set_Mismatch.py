# 1. Using hash set
# Time Complexity - O(n)
# Space Complexity - O(n)

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        set_sum = sum(set(nums))
        dsum = sum(nums)
        total = (n*(n+1))//2
        diff = total - dsum
        m = total - set_sum
        d = m - diff        
        return [d, m]           

# 2. Using Math - try to find two equations for D and M (sum and sum of squares)
# Time Complexity - O(n)
# Space Complexity - O(1)
 

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        x = 0 # D - M
        y = 0 # D^2 - M^2 = (D+M)(D-M)
        for i in range(1, n+1):
            x += nums[i-1] - i
            y += nums[i-1]**2 - i**2

        d = (y + x**2)// (2*x)
        m = d - x

        return [d, m]