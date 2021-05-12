public class Solution {  
    private int patterns;  
    private boolean valid(boolean[] keypad, int from, int to) {  
        if (from==to) return false;  
        int i=Math.min(from, to), j=Math.max(from,to);  
        if ((i==1 && j==9) || (i==3 && j==7)) return keypad[5] && !keypad[to];  
        if ((i==1 || i==4 || i==7) && i+2==j) return keypad[i+1] && !keypad[to];  
        if (i<=3 && i+6==j) return keypad[i+3] && !keypad[to];  
        return !keypad[to];  
    }  
    private void find(boolean[] keypad, int from, int step, int m, int n) {  
        if (step == n) {  
            patterns ++;  
            return;  
        }  
        if (step >= m) patterns ++;  
        for(int i=1; i<=9; i++) {  
            if (valid(keypad, from, i)) {  
                keypad[i] = true;  
                find(keypad, i, step+1, m, n);  
                keypad[i] = false;  
            }  
        }  
    }  
    public int numberOfPatterns(int m, int n) {  
        boolean[] keypad = new boolean[10];  
        for(int i=1; i<=9; i++) {  
            keypad[i] = true;  
            find(keypad, i, 1, m, n);  
            keypad[i] = false;  
        }  
        return patterns;  
    }  
} 
