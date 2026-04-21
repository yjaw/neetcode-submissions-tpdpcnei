class Solution {
    private int[] helper(char[] s, int left, int right) {
        while (left >= 0 && right < s.length && s[left] == s[right]) {
            left -= 1;
            right += 1;
        }

        return new int[] {left, right};
    }

    public String longestPalindrome(String s) {
        if (s.length() <= 1) return s;
        int[] res = new int[] {0, 0};
        char[] cs = s.toCharArray();
        for (int i = 0; i < cs.length - 1; i++) {
            int[] temp = helper(cs, i, i);
            if (temp[1] - temp[0] > res[1] - res[0]) res = temp;
            temp = helper(cs, i, i + 1);
            if (temp[1] - temp[0] > res[1] - res[0]) res = temp;
        }

        return s.substring(res[0] + 1, res[1]);
    }
}
