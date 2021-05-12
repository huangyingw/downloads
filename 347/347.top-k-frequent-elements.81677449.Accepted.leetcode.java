public class Solution 
{
    public List<Integer> topKFrequent(int[] nums, int k) 
    {
        Map<Integer, Integer> hashmap = new HashMap<Integer, Integer>();
        PriorityQueue<Map.Entry<Integer, Integer>> heap = new PriorityQueue<Map.Entry<Integer, Integer>>(
            new Comparator<Map.Entry<Integer, Integer>>() 
            {
                public int compare(Map.Entry<Integer, Integer> e1, Map.Entry<Integer, Integer> e2) 
                {
                    return e1.getValue() - e2.getValue();
                }
            });
            
        for (int i = 0; i < nums.length; i++) 
        {
            if (!hashmap.containsKey(nums[i])) 
            {
                hashmap.put(nums[i], 1);
            } 
            else 
            {
                hashmap.put(nums[i], hashmap.get(nums[i]) + 1);
            }
        }
        
        for (Map.Entry<Integer, Integer> entry : hashmap.entrySet()) 
        {
            if (heap.size() < k) 
            {
                heap.offer(entry);
            } 
            else if (heap.peek().getValue() < entry.getValue()) 
            {
                heap.poll();
                heap.offer(entry);
            }
        }
        
        List<Integer> ans = new ArrayList<Integer>();
        
        for (Map.Entry<Integer, Integer> entry : heap)
        {
            ans.add(entry.getKey());
        }
        
        return ans;
    }
}
