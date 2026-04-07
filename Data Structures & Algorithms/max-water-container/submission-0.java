class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int res = 0;
        while (left < right) {
            int water = (right - left) * Math.min(heights[left], heights[right]);
            if (water > res) res = water;
            if (heights[left] > heights[right]) right -= 1;
            else left += 1;
        }
        return res;
        
    }
}
