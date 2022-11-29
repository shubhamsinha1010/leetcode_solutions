class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in row or j in col:
                    matrix[i][j] = 0
        """
        Do not return anything, modify matrix in-place instead.
        """
        