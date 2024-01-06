# Recursion (TLE)
# Time Complexity - O(n^2)
# Space Complexity - O(n)

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort by start time
        sep = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        def backtrack(i):
            if i==len(sep):
                return 0
            
            # don't include i
            res = backtrack(i+1)
            # include
            j = i+1
            while(j<len(sep) and sep[j][0]<sep[i][1]):
                j+=1

            return max(res, backtrack(j)+sep[i][2])

        return backtrack(0)

# Recursion + memoization (TLE)
# Time Complexity - O(n^2)
# Space Complexity - O(n)

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort by start time
        sep = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        cache = [-1]*len(sep)
        def backtrack(i):
            if i==len(sep):
                return 0
            if cache[i]!=-1:
                return cache[i]
            # don't include i
            res = backtrack(i+1)
            # include
            j = i+1
            while(j<len(sep) and sep[j][0]<sep[i][1]):
                j+=1

            cache[i] = max(res, backtrack(j)+sep[i][2])
            return cache[i]

        return backtrack(0)

# Recursion + memoization + binary search
# Time Complexity - O(nlogn)
# Space Complexity - O(n)

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort by start time
        sep = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        cache = [-1]*len(sep)
        def backtrack(i):
            if i==len(sep):
                return 0
            if cache[i]!=-1:
                return cache[i]
            # don't include i
            res = backtrack(i+1)
            # include
            l = i+1
            h = len(sep)-1
            while(l<=h):
                mid = (l+h)//2
                if sep[mid][0]>=sep[i][1]:
                    if sep[mid-1][0]<sep[i][1]:
                        break
                    else:
                        h = mid-1
                else:
                    l = mid+1

            if l>h:
                mid = len(sep)

            cache[i] = max(res, backtrack(mid)+sep[i][2])
            return cache[i]

        return backtrack(0)
