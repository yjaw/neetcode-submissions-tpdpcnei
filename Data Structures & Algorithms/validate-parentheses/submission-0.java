class Solution {
    public boolean isValid(String s) {
        var que = new ArrayDeque<Character>();
        var map = new HashMap<Character, Character>();
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');
        for (char c: s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                que.push(c);
            }
            else {
                if (que.isEmpty() || map.get(c) != que.pop()) {
                    return false;
                }
            }
        }
        if (que.isEmpty()) return true;
        return false;
    }
}
