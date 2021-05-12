public class Solution 
{
    public List<Integer> topKFrequent(int[] nums, int k) 
    {
        Map<Integer, Integer> hashmap = new HashMap<Integer, Integer>();
        PriorityQueue<Map.Entry<Integer, Integer>> queue = new PriorityQueue<Map.Entry<Integer, Integer>>(
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
            } else 
            {
                hashmap.put(nums[i], hashmap.get(nums[i]) + 1);
            }
        }
        
        for (Map.Entry<Integer, Integer> entry : hashmap.entrySet()) 
        {
            if (queue.size() < k) 
            {
                queue.offer(entry);
            } 
            else if (queue.peek().getValue() < entry.getValue()) 
            {
                queue.poll();
                queue.offer(entry);
            }
        }
        
        List<Integer> ans = new ArrayList<Integer>();
        
        for (Map.Entry<Integer, Integer> entry : queue)
        {
            ans.add(entry.getKey());
        }
        
        return ans;
    }
}
