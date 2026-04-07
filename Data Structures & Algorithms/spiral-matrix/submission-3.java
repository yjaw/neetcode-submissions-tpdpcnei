class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        int left = 0;
        int right = matrix[0].length - 1;
        int top = 0;
        int bot = matrix.length - 1;

        while (left <= right && top <= bot) {
            for (int i = left; i <= right; i++) res.add(matrix[top][i]);
            top += 1;
            for (int i = top; i <= bot; i++) res.add(matrix[i][right]);
            right -= 1;
            if (left > right || top > bot) break;
            for (int i = right; i >= left; i--) res.add(matrix[bot][i]);
            bot -= 1;
            for (int i = bot; i >= top; i--) res.add(matrix[i][left]);
            left += 1;
        }

        return res;
    }
}
