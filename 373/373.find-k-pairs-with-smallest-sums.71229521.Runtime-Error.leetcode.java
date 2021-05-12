public class Solution {
    public List<int[]> kSmallestPairs(int[] nums1, int[] nums2, int k) {  
    List<int[]> res = new ArrayList<int[]>();  
    boolean visit[][] = new boolean[nums1.length][nums2.length];  
    Queue<int[]> heap = new PriorityQueue<int[]>(new Comparator<int[]>(){  
        public int compare(int[] i, int[] j) {  
            return (nums1[i[0]] + nums2[i[1]] -( nums1[j[0]] + nums2[j[1]]));  
        }  
    });  
  
    heap.add(new int[] { 0, 0 });  
    visit[0][0] = true;  
  
    while (!heap.isEmpty() && res.size() < k) {  
        int d[] = heap.poll();  
        res.add(new int[] { nums1[d[0]], nums2[d[1]] });  
  
        if (d[1] + 1 < nums2.length && visit[d[0]][d[1] + 1] == false) {  
            heap.add(new int[] { d[0], d[1] + 1 });  
            visit[d[0]][d[1] + 1] = true;  
        }  
        if (d[0] + 1 < nums1.length && visit[d[0]+1][d[1]] == false) {  
            heap.add(new int[] { d[0]+1, d[1]});  
            visit[d[0]+1][d[1]] = true;  
        }  
    }  
    return res;  
}
}
