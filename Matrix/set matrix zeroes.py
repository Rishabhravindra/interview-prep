from collections import defaultdict
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # instead of using a matrix of mn space,
        # use two matrices that keep track of rows and cols with 0 in it
        # idea is to keep track of location of row, col that has 0 not necessarily the exact location
        loc_row = [False]*len(matrix)
        loc_col = [False]*len(matrix[0])
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    loc_row[row] = True
                    loc_col[col] = True
                    
        def zerofy_row(row):
            for col in range(len(matrix[0])):
                matrix[row][col] =0
        
        def zerofy_col(col):
            for row in range(len(matrix)):
                matrix[row][col] =0
        
        for row in range(len(loc_row)):

            if loc_row[row]:
                zerofy_row(row)

        for col in range(len(loc_col)):
            if loc_col[col]:
                zerofy_col(col)
                
        