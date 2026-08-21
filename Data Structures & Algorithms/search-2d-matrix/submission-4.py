class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        lo = 0
        hi = rows * cols - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            row = mid // cols
            col = mid % cols
            print(mid, row, col)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False