public class Solution {
    public int[] getModifiedArray(int length, int[][] updates) {
    int[] result = new int[length];
    if(updates==null||updates.length==0)
        return result;
 
    for(int i=0; i<updates.length; i++){
        result[updates[i][0]] += updates[i][2];
        if(updates[i][1]<length-1){
            result[updates[i][1]+1] -=updates[i][2];
        }
    }
 
    int v=0;
    for(int i=0; i<length; i++){
        v += result[i];
        result[i]=v;
    }
 
    return result;
}
}
