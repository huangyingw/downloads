public class Solution {
    public List<String> generateAbbreviations(String word){
        List<String> res = new ArrayList<String>();
        backtrack(res, word, 0, "", 0);
        return res;
    }

    private void backtrack(List<String> res, String word, int pos, String cur, int count){
        if(pos==word.length()){
            if(count > 0)
                cur += count;
            res.add(cur);
        }
        else{
            backtrack(res,word,pos+1,cur, count+1);
            backtrack(res,word,pos+1,cur+(count>0?count:"")+word.charAt(pos),0);
        }
    }
}

