# Time Complexity - O(nlogn)
# Space Complexity - O(n)

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wdict, ldict = {}, {}
        res = [[], []]
        for w, l in matches:
            wdict[w] = wdict.get(w, 0) + 1
            ldict[l] = ldict.get(l, 0) + 1

        for k, v in wdict.items():
            if k not in ldict:
                res[0].append(k)

        for k, v in ldict.items():
            if v==1:
                res[1].append(k)
        
        return [sorted(res[0]), sorted(res[1])]