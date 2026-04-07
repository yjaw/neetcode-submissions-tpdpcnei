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
    public boolean canAttendMeetings(List<Interval> intervals) {
        intervals.sort((a, b) -> Integer.compare(a.start, b.start));
        Interval cur = new Interval(0, 0);
        for (Interval interval: intervals) {
            if (cur.end > interval.start) return false;
            cur = interval;
        }
        return true;
    }
}
