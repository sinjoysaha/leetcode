'''
Intuition
First, we count of frequency of each element in the array.
For each of the frequencies n, we have to find the minimum steps to reduce it to zero.
Any number n>1, can be expressed as n=2p+3q where p,q ϵ W.
So, essentially the problem is to express nnn as 2p+3q such that p+q is minimum.

Approach
1. Count of frequency of each element and store it in a dictionary.
2. Iterate through the keys of the dict.
3. If any freq. is 1, return -1.
4. Else, check n % 3. So, 3 possibilities -> (0, 1, 2)
5. If n % 3 == 0, min. steps will be n/3.
6. If n % 3 != 0, min. steps will be (n//3)−1+2 = (n//3)+1.

Steps 4, 5, 6 can be combined into the following.
    min_step =  n//3 + (n%3 != 0)

Explanation for Step 6.
If n % 3 == 1, min. steps will be (n//3)−1 + (1+3)//2. 
This is because n = 3k + 1 = 3(k-1) + 4 = 3(k-1) + 2*2, so min. steps = (k-1) + 2 = k+1.

If n % 3 == 2, min. steps will be (n//3) + 1 as the 2 can be reduced directly. 
This is because n = 3k + 2 = 3k + 2*1, so min. steps = k+1.

Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq_dict = {}
        steps = 0
        for n in nums:
            freq_dict[n] = freq_dict.get(n, 0) + 1

        print(freq_dict)
        for k in freq_dict:
            if freq_dict[k]==1:
                return -1

            steps += freq_dict[k]//3 + (freq_dict[k]%3 != 0)

        return steps
