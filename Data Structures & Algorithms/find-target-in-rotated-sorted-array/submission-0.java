class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        int m = l + (r - l) / 2;
        
        while (l <= r) {
            m = l + (r - l) / 2;
            if (nums[m] == target) return m;

            if (nums[l] <= nums[m]) {
                if (nums[l] <= target && target <= nums[m]) {
                    r = m;
                }
                else {
                    l = m + 1;
                }
            }
            else {
                if (nums[m] <= target && target <= nums[r]) {
                    l = m;
                }
                else {
                    r = m - 1;
                }
            }
        }
        return -1;
    }
}
