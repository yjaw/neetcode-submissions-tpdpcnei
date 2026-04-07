class Solution {
    public int[] countBits(int n) {
        int[] res = new int[n + 1]; // 0 ~ n
        for (int i = 0; i < n + 1; i++) {
            int num = i;
            int count = 0;
            while (num % 2 == 1) {
                count += 1;
                num >>= 1;
            }
            count += res[num / 2];
            res[i] = count;
        }
        return res;
    }
}
