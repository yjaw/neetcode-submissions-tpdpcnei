class Solution {
    public int maxSubArray(int[] nums) {
        int res = -20000;
        int sum = -20000;
        for (int num: nums) {
            if (num > sum + num) sum = num;
            else sum += num;
            res = Math.max(res, sum);
        }
        return res;
    }
}
