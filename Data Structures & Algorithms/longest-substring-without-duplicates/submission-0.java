class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int right = 0;
        var mem = new HashSet<Character>();
        int res = 0;
        while (right < s.length()) {
            var new_char = s.charAt(right);
            while (mem.contains(new_char)) {
                mem.remove(s.charAt(left));
                left += 1;
            }
            mem.add(new_char);
            res = Math.max(res, mem.size());
            right += 1;
        }
        return res;
    }
}
