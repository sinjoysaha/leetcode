# Freq of Freq should match
# Time Complexity - O(n)
# Space Complexity - O(n)

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        freq1, freq2 = {}, {}
        for c in word1:
            freq1[c] = freq1.get(c, 0) + 1
        for c in word2:
            freq2[c] = freq2.get(c, 0) + 1

        if freq1.keys()!=freq2.keys():
            return False

        cofreq1, cofreq2 = {}, {}
        for k, v in freq1.items():
            cofreq1[v] = cofreq1.get(v, 0) + 1
        for k, v in freq2.items():
            cofreq2[v] = cofreq2.get(v, 0) + 1

        return cofreq1==cofreq2