class Solution {
    public int longestConsecutive(int[] nums) {
        var nums_set = new HashSet<Integer>();
        for (int num: nums) {
            nums_set.add(num);
        }
        var res = 0;
        for (int start: nums) {
            if (!nums_set.contains(start - 1)) {
                var end = start;
                while (nums_set.contains(end)) {
                    end += 1;
                }
                if ((end - start) > res) res = (end - start);
            }

        }
        return res;
    }
}
