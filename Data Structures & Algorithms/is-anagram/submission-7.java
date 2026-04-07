class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Integer> mem = new HashMap<>();
        for (char c: s.toCharArray()) {
            mem.put(c, mem.getOrDefault(c, 0) + 1);
        }
        for (char c: t.toCharArray()) {
            mem.put(c, mem.getOrDefault(c, 0) - 1);
            if (mem.get(c) < 0) {
                return false;
            }
        }
        return true;
    }
}
