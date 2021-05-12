public class Solution {
    public int longestValidParentheses(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }    

        // in this case, res[i] means the max length of parensis ended at i; if not, then res[i] = 0
        int[] res = new int[s.length()];
        int open = 0, max = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                open++;
                //res[i] = res[i-1];
            } else {
                if (open > 0) {
                    res[i] = res[i-1] + 2;
                    // important lines here
                    if (i >= res[i]) {
                        res[i] += res[i-res[i]];
                    }
                    open--;
                }
            }

            max = Math.max(max, res[i]);
        }

        return max;
    }
}
