class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> hmap = new HashMap<>();

        for (String str: strs) {
            int[] count = new int[26];
            for (char c: str.toCharArray()) {
                count[c - 'a'] += 1;
            }
            StringBuilder sb = new StringBuilder();
            for (int i: count) {
                sb.append(i).append('/');
            }
            String key = sb.toString();
            hmap.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
        }
        return new ArrayList<>(hmap.values());
    }
}
