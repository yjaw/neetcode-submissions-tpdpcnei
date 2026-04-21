class Solution {
    private int helper(char[] cs, int left, int right) {
        int count = 0;
        while (left >= 0 && right < cs.length && cs[left] == cs[right]) {
            count ++;
            left --;
            right ++;
        }

        return count;
    }
    public int countSubstrings(String s) {
        if (s.length() <= 1) return s.length();

        int res = 0;
        char[] cs = s.toCharArray();
        for (int i = 0; i < cs.length; i++) {
            res += helper(cs, i, i);
            res += helper(cs, i, i + 1);
        }
        
        return res;
    }
}
