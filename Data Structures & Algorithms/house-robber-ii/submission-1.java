class Solution {
    public int rob(int[] nums) {
        int res1 = 0;
        int res2 = 0;
        int maxProfit1 = 0;
        int maxProfit2 = 0;
        if (nums.length == 1) return nums[0];
        for (int i = 0; i < nums.length - 1; i++) {
            if (i == 0) {
                maxProfit1 = nums[i];
            }
            else if (i == 1) {
                maxProfit2 = Math.max(maxProfit1, nums[i]);
            }
            else {
                int curProfit = Math.max(maxProfit1 + nums[i], maxProfit2);
                maxProfit1 = maxProfit2;
                maxProfit2 = curProfit;
            }
        }
        res1 = Math.max(maxProfit1, maxProfit2);

        maxProfit1 = 0;
        maxProfit2 = 0;

        for (int i = 1; i < nums.length; i++) {
            if (i == 1) {
                maxProfit1 = nums[i];
            }
            else if (i == 2) {
                maxProfit2 = Math.max(maxProfit1, nums[i]);
            }
            else {
                int curProfit = Math.max(maxProfit1 + nums[i], maxProfit2);
                maxProfit1 = maxProfit2;
                maxProfit2 = curProfit;
            }
        }
        res2 = Math.max(maxProfit1, maxProfit2);

        return Math.max(res1, res2);
    }
}
