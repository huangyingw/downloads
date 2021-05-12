public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int count=0;
        while(n!=0) 
        {
            if(n%2 !=0)
            {
                count++;
            }
            n/=2;    
        }
        return count;
    }
}
