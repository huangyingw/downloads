/* The knows API is defined in the parent class Relation.
      boolean knows(int a, int b); */
 
public class Solution extends Relation {
    public int findCelebrity(int n) {
        if(n <=1) return 0;
         
        //Below is the elimination process. If the left people knows right, we will eliminate left person, which is left++; else we will eliminate the right person, which is the step right--. After we go through all these steps, we'll know that only one person is left that satisfies our logic.
        int left = 0;
        int right = n-1;
        while(left < right){
            if(knows(left, right)) left++;
            else right--;
        }
         
        //Last but not least, here we need to check whether the only person is the real celebrity. Consider one example, if A does not know B and B does not know A either, then A and B would not be celebrity. So we need to check the negative case, which is left knows some person or any person does not know the left person.
        for(int i = 0; i < n; i++){
            if(i != left){
                if(knows(left, i) || !knows(i, left)) return -1;
            }
        }
         
        return left;
    }
}
