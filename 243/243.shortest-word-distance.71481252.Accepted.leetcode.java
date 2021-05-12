public class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        int idx1 = -1, idx2 = -1, distance = Integer.MAX_VALUE;
        for(int i = 0; i < words.length; i++){
            if(words[i].equals(word1)){
                idx1 = i;
                // 第一次写入idx就先不比较
                if(idx2 != -1) distance = Math.min(distance, idx1 - idx2);
            }
            if(words[i].equals(word2)){
                idx2 = i;
                // 第一次写入idx就先不比较
                if(idx1 != -1) distance = Math.min(distance, idx2 - idx1);
            }
        }
        return distance;
    }
}
