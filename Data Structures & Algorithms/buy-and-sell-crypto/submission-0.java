class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        int cur_price = Integer.MAX_VALUE;
        
        for (int price: prices) {
            if (price < cur_price) {
                cur_price = price;
            }
            res = Math.max(res, price - cur_price);
            
            
        }
        return res;
    }
}
