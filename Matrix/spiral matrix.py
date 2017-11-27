class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # track directions R, B,L, U
        # border cases  left_col, right_col, top_row, bot_row0
        # direcction 0(L-> R),1 (T->B),2(R->L),3(B-> T)
        if len(matrix) ==0: return []
        path = []
        direction = 0
        top_row = left_col = 0
        bot_row = len(matrix)-1
        right_col = len(matrix[0])-1
        while left_col <= right_col and top_row <= bot_row:
            if direction == 0:
                for i in range(left_col, right_col+1):
                    path.append(matrix[top_row][i])
                top_row += 1                    
            
            elif direction == 1:
                for i in range(top_row, bot_row+1):
                    path.append(matrix[i][right_col])
                right_col -= 1
                
            elif direction == 2:
                for i in range(right_col, left_col-1,-1):
                    path.append(matrix[bot_row][i])
                bot_row -= 1                    
            elif direction == 3:
                for i in range(bot_row, top_row-1, -1,):
                    path.append(matrix[i][left_col])
                left_col += 1                    
            direction = (direction+1)%4
        return path
                    