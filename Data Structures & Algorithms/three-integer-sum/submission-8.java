class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        var res = new ArrayList<List<Integer>>();

        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length - 2; i++) {
            if (nums[i] > 0) break; 
            if (i > 0 && nums[i - 1] == nums[i]) continue;

            var left = i + 1;
            var right = nums.length - 1;
            while (left < right) {
                if (nums[left] + nums[right] + nums[i] == 0) {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left += 1;
                    right -= 1;
                    while (left < right && nums[left] == nums[left - 1]) left += 1; 
                }
                else if (nums[left] + nums[right] + nums[i] < 0) left += 1;
                else right -= 1;
            
            }
        }
        return res;
    }
}
