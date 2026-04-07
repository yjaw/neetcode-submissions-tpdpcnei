class Solution {
    public String minWindow(String s, String t) {
        var mem = new HashMap<Character, Integer>();
        for (char c: t.toCharArray()) {
            mem.put(c, mem.getOrDefault(c, 0) + 1);
        }
        int flag = mem.size();
        String res = s + t;
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            var c = s.charAt(right);
            if (mem.containsKey(c)) {
                mem.put(c, mem.get(c) - 1);
                if (mem.get(c) == 0) flag -= 1;
            }
            while (flag == 0) {
                if (res.length() > (right - left + 1)) {
                    res = s.substring(left, right + 1);
                }
                var lc = s.charAt(left);
                if (mem.containsKey(lc)) {
                    mem.put(lc, mem.get(lc) + 1);
                    if (mem.get(lc) == 1) flag += 1;
                }
                left += 1;
            } 
        }
        if (res.equals(s + t)) return "";
        return res;
    }
}
