public class ValidWordAbbr {
    private Set<String> uniqueDict;
    private Map<String, String> abbrDict;
 
    public ValidWordAbbr(String[] dictionary) {
        uniqueDict = new HashSet<>();
        abbrDict = new HashMap<>();
         
        for (String word : dictionary) {
            if (!uniqueDict.contains(word)) {
                String abbr = getAbbr(word);
                if (!abbrDict.containsKey(abbr)) {
                    abbrDict.put(abbr, word);
                } else {
                    abbrDict.put(abbr, "");
                }
                 
                uniqueDict.add(word);
            }
        }
    }
 
    public boolean isUnique(String word) {
        if (word == null || word.length() == 0) {
            return true;
        }
         
        String abbr = getAbbr(word);
        if (!abbrDict.containsKey(abbr) || abbrDict.get(abbr).equals(word)) {
            return true;
        } else {
            return false;
        }
    }
     
    private String getAbbr(String word) {
        if (word == null || word.length() < 3) {
            return word;
        }
         
        StringBuffer sb = new StringBuffer();
        sb.append(word.charAt(0));
        sb.append(word.length() - 2);
        sb.append(word.charAt(word.length() - 1));
         
        return sb.toString();
 
    }
     
}
 
 
// Your ValidWordAbbr object will be instantiated and called as such:
// ValidWordAbbr vwa = new ValidWordAbbr(dictionary);
// vwa.isUnique("Word");
// vwa.isUnique("anotherWord");
