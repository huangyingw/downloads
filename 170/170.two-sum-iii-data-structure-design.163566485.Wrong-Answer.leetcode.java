public class TwoSum
{
    private Map<Integer, Integer> map = new HashMap<Integer, Integer>();

    public void add(int input)
    {
        int count = map.containsKey(input) ? map.get(input) : 0;
        map.put(input, count + 1);
    }

    public boolean find(int val)
    {
        for (Map.Entry<Integer, Integer> ent : map.entrySet())
        {
            int key = ent.getKey();
            int target = val - key;

            if (map.containsKey(target))
            {
                if (key != target)
                {
                    return true;
                }
            }
        }

        return false;
    }
}

