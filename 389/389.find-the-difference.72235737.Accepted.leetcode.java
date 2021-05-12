public class Solution {
    public char findTheDifference(String s, String t) {
        Map<Character, Integer> map = new HashMap<>();
        char[] schar = s.toCharArray();
        char[] tchar = t.toCharArray();
        for (int i = 0; i < s.length(); i++) {
            if (map.containsKey(schar[i])) map.put(schar[i], map.get(schar[i])+1);
            else map.put(schar[i], 1);
        }
        for (int i = 0; i < t.length(); i++) {
            if (map.containsKey(tchar[i]) && map.get(tchar[i]) > 0) map.put(tchar[i], map.get(tchar[i])-1);
            else return tchar[i];
        }
        return 'a';
    }
}
