class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        int[] dpMax = new int[n];
        int[] dpMin = new int[n];
        dpMax[0] = nums[0];
        dpMin[0] = nums[0];
        int res = nums[0];
        for (int i = 1; i < n; i++) {
            int curMax = dpMax[i - 1] * nums[i];
            int curMin = dpMin[i - 1] * nums[i];

            dpMax[i] = Math.max(curMax, Math.max(curMin, nums[i]));
            dpMin[i] = Math.min(curMax, Math.min(curMin, nums[i]));

            res = Math.max(res, dpMax[i]);
        }

        return res; 

    }
}
