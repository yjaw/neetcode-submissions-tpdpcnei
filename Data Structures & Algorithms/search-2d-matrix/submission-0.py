class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        lo = 0
        hi = (row * col) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            x = mid // col
            y = mid - (x * col)
            print(mid, x, y)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False