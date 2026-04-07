class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length == 0) return 0;
        int res = 0;
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        int preEnd = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            int[] cur = intervals[i];
            if (cur[0] < preEnd) {
                res += 1;
                preEnd = Math.min(preEnd, cur[1]);
            }
            else {
            preEnd = cur[1];

            }
            
        }
        return res;
    }
}
