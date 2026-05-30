class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1

        left = 0
        right = len(matrix[0]) -1

        while top <= bottom:
            middle_row = top + (bottom-top)//2
            if matrix[middle_row][left] <= target and matrix[middle_row][right] >= target:
                while left <= right:
                    middle_column = left + (right-left)//2
                    if matrix[middle_row][middle_column] == target:
                        return True
                    elif matrix[middle_row][middle_column] < target:
                        left = middle_column + 1
                    elif matrix[middle_row][middle_column] > target:
                        right = middle_column - 1
                return False
            elif matrix[middle_row][left] >= target:
                bottom = middle_row - 1
            elif matrix[middle_row][right] <= target:
                top = middle_row+1
            
        return False