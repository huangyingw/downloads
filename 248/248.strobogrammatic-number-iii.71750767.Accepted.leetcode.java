public class Solution {
public int strobogrammaticInRange(String low, String high) {
    int m = low.length(), n = high.length();
    List<String> result = new ArrayList<String>();
    for(int i=m; i<=n; i++){
        result.addAll(findStrobogrammatic(i));
    }
    int i=0;
    int count=result.size();
    while(i<result.size() && result.get(i).length()==low.length()){
        if(result.get(i).compareTo(low)<0){
            count--;
        }
        i++;
    }
    i=result.size()-1;
    while(i>=0 && result.get(i).length()==high.length()){
        if(result.get(i).compareTo(high)>0){
            count--;
        }
        i--;
    }
    return count;
}
public List<String> findStrobogrammatic(int n) {
    HashMap<Character, Character> map = new HashMap<>();
    map.put('1','1');
    map.put('0','0');
    map.put('6','9');
    map.put('9','6');
    map.put('8','8');
    List<String> list = new ArrayList<>();
    char[] arr = new char[n];
    dfs(list, arr, 0, n, map);
    Collections.sort(list);
    return list;
}
public void dfs(List<String> list, char[] buffer, int idx, int n, Map<Character, Character> map){
    if(idx==(n+1)/2){
        list.add( String.valueOf(buffer));
        return;
    }
    for(char key:map.keySet()){
        if(idx==0 && n>1 && key=='0'){
            continue;
        }
        if(idx==(n/2) && (key=='6'||key=='9')){
            continue;
        } 
        buffer[idx] = key;
        buffer[n-idx-1] = map.get(key);
        dfs(list, buffer, idx+1, n, map);
    }
}
}
