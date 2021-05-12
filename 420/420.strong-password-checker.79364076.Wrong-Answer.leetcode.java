public class Solution {

    public int strongPasswordChecker(String s) {
        int sLen = s.length();
        if (sLen < 4) {
            return 6 - sLen;
        }

        int lnum = 1; // need lower
        int unum = 1; // need upper
        int dnum = 1; // need digit

        int rcount = 0;  // count need to replace repeated seq
        int ricount = 0; // count need to add in repeated seq
        int rdcount = 0; // count need to remove from repeated seq
        int sameseq = 0; // count of chars in repeated seq

        for (int i=0; i<sLen; i++) {
            char ch = s.charAt(i);
            if (ch>='a' && ch<='z') {
                lnum = 0;
            }
            if (ch>='A' && ch<='Z') {
                unum = 0;
            }
            if (ch>='0' && ch<='9') {
                dnum = 0;
            }

            // check repeated seq
            if (i == 0) {
                sameseq = 1;
            }
            else if (ch != s.charAt(i-1)) {
                if (sameseq >= 3) {
                    // if shorter length, add char into repeated seq
                    while (sLen + ricount < 6 && sameseq >= 3) {
                        ricount++;
                        sameseq -= 2;
                    }
                    // if longer length, remove char from repeated seq
                    while (sLen - rdcount > 20 && sameseq >= 3) {
                        rdcount++;
                        sameseq --;
                    }
                    // if length matches, replace char in repeated seq
                    rcount += sameseq / 3;
                }
                sameseq = 1;
            }
            else {
                sameseq++;
            }
        }

        // need check repeated seq after loop
        if (sameseq >= 3) {
            // as previous process
            while (sLen + ricount < 6 && sameseq >= 3) {
                ricount++;
                sameseq -= 2;
            }
            while (sLen - rdcount > 20 && sameseq >= 3) {
                rdcount++;
                sameseq --;
            }
            rcount += sameseq / 3;
        }

        int update = lnum + unum + dnum;
        int must = ricount + rcount;
        if (sLen + ricount < 6) {
            must += 6 - sLen - ricount;
        }
        if (sLen < 20) {
            return must > update ? must : update;
        }

        // if longer length, use below process
        if (sLen - rdcount > 20) {
            rdcount += sLen - rdcount - 20;
        }
        return rcount >= update ? rcount + rdcount : update + rdcount;

    }
    
}
