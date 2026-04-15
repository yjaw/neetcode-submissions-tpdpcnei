class Solution {
    public int rob(int[] nums) {
        int[] rob = new int[nums.length];
        int[] notRob = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (i < 2) {
                rob[i] = nums[i];
                if (i == 0) notRob[i] = 0;
                if (i == 1) notRob[i] = rob[0];
            }
            else {
                rob[i] = nums[i] + Math.max(rob[i - 2], notRob[i - 1]);
                notRob[i] = Math.max(rob[i - 1], notRob[i - 1]);
            }
        }
        return nums.length == 0 ? 0 : Math.max(rob[nums.length - 1], notRob[nums.length - 1]);
    }
}
