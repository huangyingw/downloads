public class ValidWordAbbr {
    private Map<String, String> map = new HashMap<String, String>();

    public ValidWordAbbr(String[] dictionary) {
        for(int i = 0; i < dictionary.length; i++){
            String key = abbreviate(dictionary[i]);
            if(!map.containsKey(key)){
                map.put(key, dictionary[i]);
            }else{
                map.put(key, "");
            }
        }
    }
    
    private String abbreviate(String str){
        return str.charAt(0) + Integer.toString(str.length() - 2)+ str.charAt(str.length()-1);
    }

    public boolean isUnique(String word) {
        String x = abbreviate(word);
        if(map.containsKey(x)){
            if(map.get(x).equals(word)){
                return true;
            }else {
                return false;
            }
        }
        return true;
    }
}

// Your ValidWordAbbr object will be instantiated and called as such:
// ValidWordAbbr vwa = new ValidWordAbbr(dictionary);
// vwa.isUnique("Word");
// vwa.isUnique("anotherWord");
