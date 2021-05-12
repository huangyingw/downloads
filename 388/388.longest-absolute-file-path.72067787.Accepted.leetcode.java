public class Solution {
    public int lengthLongestPath(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }
        String[] files = s.split("\n");
        int maxLen = 0;
        int pathLen = 0;
        Stack<Integer> dirLen = new Stack<>();
        for (int i = 0; i < files.length; i++) {
            String curLine = files[i];
            int curLvl = findLvl(curLine);
            int lvDiff = dirLen.size() - curLvl;
            while (lvDiff > 0) {
                pathLen -= dirLen.pop();
                lvDiff -= 1;
            }
            int dotPos = curLine.indexOf('.');
            if (dotPos > -1) {
                maxLen = Math.max(maxLen, pathLen + curLine.length() - curLvl);
            } else {
                pathLen += curLine.length() - curLvl + 1;
                dirLen.push(curLine.length() - curLvl + 1);
            }
        }
        return maxLen;
    }
 
    private int findLvl(String s) {
        int count = 0;
        while (s.charAt(count) == '\t') {
            count += 1;
        }
        return count;
    }
}
