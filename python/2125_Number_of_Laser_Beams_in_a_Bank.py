# Keep track of prev. #devices
# Time Complexity - O(nm)

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        prev = 0
        for r in bank:
            curr = 0
            for c in r:
                curr += int(c)

            if not curr:
                continue
            else:
                total += prev*curr
                prev = curr

        return total