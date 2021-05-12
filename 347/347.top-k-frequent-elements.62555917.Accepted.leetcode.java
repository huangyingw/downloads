    public class Solution
    {
        public List<Integer> topKFrequent(int[] nums, int k)
        {
            // count the frequency for each element
            HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
            for (int num : nums)
            {
                if (map.containsKey(num))
                {
                    map.put(num, map.get(num) + 1);
                }
                else
                {
                    map.put(num, 1);
                }
            }
            // get the max frequency
            int max = 0;
            for (Map.Entry<Integer, Integer> entry : map.entrySet())
            {
                max = Math.max(max, entry.getValue());
            }
            // initialize an array of ArrayList. index is frequency, value is
            // list of numbers
            ArrayList<Integer>[] arr =
                (ArrayList<Integer>[]) new ArrayList[max + 1];
            for (int i = 1; i <= max; i++ )
            {
                arr[i] = new ArrayList<Integer>();
            }
            for (Map.Entry<Integer, Integer> entry : map.entrySet())
            {
                int count = entry.getValue();
                int number = entry.getKey();
                arr[count].add(number);
            }
            List<Integer> result = new ArrayList<Integer>();
            // add most frequent numbers to result
            for (int j = max; j >= 1; j-- )
            {
                if (arr[j].size() > 0)
                {
                    for (int a : arr[j])
                    {
                        result.add(a);
                    }
                }
                if (result.size() == k)
                {
                    break;
                }
            }
            return result;
        }
    }

