class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        //Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> res = new ArrayList<>();
        int[] pre = newInterval;
        for (int i = 0; i < intervals.length; i++) {
            int[] cur = intervals[i];

            if (pre[1] < cur[0]) {
                res.add(pre);
                pre = cur;
            }
            else if (pre[0] > cur[1]) {
                res.add(cur);
            }
            else {
                pre[0] = Math.min(pre[0], cur[0]);
                pre[1] = Math.max(pre[1], cur[1]);
            }
        }
        res.add(pre);
        return res.toArray(new int[res.size()][]);
    }
}
