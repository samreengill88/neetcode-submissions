class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top_row = 0
        bottom_row = ROWS - 1
        

        # find the row where you can search the target 
        while top_row <= bottom_row:
            # find middle row 
            mid_row = (top_row + bottom_row) // 2
            
            # compare target to last element of mid_row -> to get last element of list-> -1 
            if target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            
            # compare to first element of mid row
            elif target < matrix[mid_row][0]:
                bottom_row = mid_row - 1
            else: break 
        
        row = (top_row + bottom_row) // 2
        l = 0
        r = COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False
                
# TC: O(log (m * n)) m is no of rows, n is no of cols
# SC: O(1)