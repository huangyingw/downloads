public class Solution
{
    public String largestNumber(int[] nums)
    {
        StringBuilder result = new StringBuilder();
        List<Integer> datas = new ArrayList<Integer>();

        for (int i : nums)
        {
            datas.add(i);
        }

        Collections.sort(datas, new Comparator<Integer>()
        {
            @Override
            public int compare(Integer o1, Integer o2)
            {
                return (o2 + "" + o1).compareTo(o1 + "" + o2);
            }
        });
        boolean isFirst = true;

        for (int data : datas)
        {
            if (data == 0)
            {
                if (!isFirst)
                {
                    continue;
                }
                else
                {
                    isFirst = false;
                }
            }

            result.append(data);
        }

        return result.toString();
    }
}

