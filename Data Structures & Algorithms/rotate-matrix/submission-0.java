class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;
        // top-left flip to bot-right
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m - i; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n - 1 - j][m - 1 - i];
                matrix[n - 1 - j][m - 1 - i] = temp;
            }
        }

        // flip upside down
        for (int i = 0; i < n / 2; i++) {
            for (int j = 0; j < m; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n - 1 -i][j];
                matrix[n - 1 - i][j] = temp;
            }
        }
        
        return;
    }
}
