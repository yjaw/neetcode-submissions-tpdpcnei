class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0 || s.charAt(0) == '0') return 0;

        int n = s.length();
        // dp[i] 表示長度為 i 的字串有多少種解法
        int[] dp = new int[n + 1];
        dp[0] = 1; // 空字串
        dp[1] = 1; // 長度為 1 且不為 '0'

        for (int i = 2; i <= n; i++) {
            // 情況 1：檢查當前字元（單個數字）
            int oneDigit = s.charAt(i - 1) - '0';
            if (oneDigit >= 1 && oneDigit <= 9) {
                dp[i] += dp[i - 1];
            }

            // 情況 2：檢查當前與前一個字元（雙個數字）
            int twoDigits = Integer.parseInt(s.substring(i - 2, i));
            if (twoDigits >= 10 && twoDigits <= 26) {
                dp[i] += dp[i - 2];
            }
        }

        return dp[n];
    }
}