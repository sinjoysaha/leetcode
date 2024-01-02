# Use hash set or freq dict.
# Time Complexity - O(n)

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq_dict = {}
        max_count = 0
        for n in nums:
            freq_dict[n] = freq_dict.get(n, 0) + 1
            max_count = max(max_count, freq_dict[n])
            
        m = [[] for i in range(max_count)]
        for n in freq_dict:
            while freq_dict[n] > 0:
                m[freq_dict[n]-1].append(n)
                freq_dict[n] -= 1
            
        return m