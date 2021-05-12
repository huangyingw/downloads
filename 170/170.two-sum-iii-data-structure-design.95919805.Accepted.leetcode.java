public class TwoSum
{
    private Map<Integer, Integer> map = new HashMap<Integer, Integer>();

    public void add(int input)
    {
        if (!map.containsKey(input))
        {
            map.put(input, 0);
        }
        
        map.put(input, map.get(input) + 1);
    }

    public boolean find(int val)
    {
        for (Map.Entry<Integer, Integer> ent : map.entrySet())
        {
            int key = ent.getKey();
            int target = val - key;
            
            if (key == target)
            {
                if (ent.getValue() > 1)
                {
                    return true;    
                }
                else
                {
                    continue;
                }
            }
            
            if (map.containsKey(target))
            {
                return true;
            }
        }
        
        return false;
    }
}
