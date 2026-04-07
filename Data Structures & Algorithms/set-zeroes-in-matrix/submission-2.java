class Solution {
    public void setZeroes(int[][] matrix) {
        boolean zeroInRow = false;
        boolean zeroInCol = false;
        int row = matrix.length;
        int col = matrix[0].length;
        
        for (int i = 0; i < row; i++) {
            if (matrix[i][0] == 0) {
                zeroInRow = true;
                break;
            }
        }

        for (int j = 0; j < col; j++) {
            if (matrix[0][j] == 0) {
                zeroInCol = true;
                break;
            }
        }

        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for (int i = 1; i < row; i++) {
            if (matrix[i][0] == 0) {
                for (int j = 1; j < col; j++) matrix[i][j] = 0;
            }
        }

        for (int j = 1; j < col; j++) {
            if (matrix[0][j] == 0) {
                for (int i = 1; i < row; i++) matrix[i][j] = 0;
            }
        }

        if (zeroInRow) {
            for (int i = 0; i < row; i++) matrix[i][0] = 0;
        }

        if (zeroInCol) {
            for (int j = 0; j < col; j++) matrix[0][j] = 0;
        }

        return;
    }
}
