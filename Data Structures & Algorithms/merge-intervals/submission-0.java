class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> res = new ArrayList<>();
        int[] pre = intervals[0];
        for (int i = 1; i < intervals.length; i++) {
            int[] cur = intervals[i];

            if (cur[0] <= pre[1]) {
                pre[1] = Math.max(pre[1], cur[1]);
            }
            else {
                res.add(pre);
                pre = cur;
            } 
        }
        res.add(pre);
        return res.toArray(new int[res.size()][]);
    }
}
