class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        int m = (l + r) / 2;
        
        while (l <= r) {
            if (nums[l] <= nums[r]) {
                return nums[l];
            }
            m = (l + r) / 2;
            if (nums[l] <= nums[m]) {
                l = m + 1;
            }
            else {
                r = m;
            }
        }
        return -1001;
    }
}
