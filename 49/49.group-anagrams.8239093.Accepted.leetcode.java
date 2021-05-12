  public class Solution {
    public ArrayList<String> anagrams(String[] strs) {
      Map<String, List<String>> dict = new HashMap<String, List<String>>();

      for (String str : strs) {
        char[] cs = str.toCharArray();
        Arrays.sort(cs);
        String anagram = new String(cs);
        List<String> l = dict.get(anagram);

        if (l == null) {
          l = new ArrayList<String>();
          dict.put(anagram, l);
        }

        l.add(str);
      }

      ArrayList<String> ans = new ArrayList<String>();
      Iterator<List<String>> iter = dict.values().iterator();

      while (iter.hasNext()) {
        ArrayList<String> item = (ArrayList<String>) iter.next();

        if (item.size() > 1) {
          ans.addAll(item);
        }
      }

      return ans;
    }
  }

