/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        int res = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        intervals.sort((a, b) -> Integer.compare(a.start, b.start));
        for (Interval cur: intervals) {
            while (pq.size() != 0 && pq.peek() <= cur.start) pq.poll();
            pq.offer(cur.end);
            res = Math.max(res, pq.size());
        }
        return res;
    }
}
