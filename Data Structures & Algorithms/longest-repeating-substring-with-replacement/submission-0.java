class Solution {
    int helper(int[] mem) {
        int cur_sum = 0;
        int cur_max = 0;
        for (int count: mem) {
                cur_sum += count;
                cur_max = Math.max(cur_max, count);
            }
        return (cur_sum - cur_max);
    }
    public int characterReplacement(String s, int k) {
        int left = 0;
        int right = 0;
        int res = 0;
        int cur_k = 0;
        var mem = new int[26];

        while (right < s.length()) {
            mem[s.charAt(right) - 'A'] += 1;
            right += 1;
            cur_k = helper(mem);
            while (cur_k > k) {
                mem[s.charAt(left) - 'A'] -= 1;
                left += 1;
                cur_k = helper(mem);
            }
            res = Math.max(res, (right - left));
        }
        return res;
    }
}
