# Time Complexity - O(n^2)
# Space Complexity - O(n^2) if the input matrix is kept unchanged else O(1)

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for r in range(n-2, -1, -1):
            for c in range(n):
                if c==0:
                    matrix[r][c] = matrix[r][c]+min(matrix[r+1][c], matrix[r+1][c+1])
                elif c==len(matrix)-1:
                    matrix[r][c] = matrix[r][c]+min(matrix[r+1][c-1], matrix[r+1][c])
                else:
                    matrix[r][c] = matrix[r][c]+min(matrix[r+1][c-1], matrix[r+1][c], matrix[r+1][c+1])

        return min(matrix[0])