class Solution {
    public int getSum(int a, int b) {
        int res = 0;
        int carry = 0;

        for (int i = 0; i < 32; i++) {
            int bitA = (a >> i) & 1;
            int bitB = (b >> i) & 1;
            int bitCur = bitA ^ bitB ^ carry;
            carry = bitA + bitB + carry >= 2 ? 1 : 0;

            if (bitCur == 1) {
                res = res | (1 << i);
            }    
        }
        
        return res;
    }
}
