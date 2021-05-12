/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int L = 1,R = n;
        while(L <= R){
            int mid = L + ((R - L) >> 1);
            int res = guess(mid);
            if(res == 0) return mid;
            else if(res == 1)  L = mid + 1;
            else R = mid - 1;
        }
        return L;
    }
}
