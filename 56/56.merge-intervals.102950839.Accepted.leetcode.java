public class Solution
{
    public List<Interval> merge(List<Interval> intervals)
    {
        Collections.sort(intervals, new Comparator<Interval>() 
        {
            @Override
            public int compare(Interval o1, Interval o2)
            {
                if(o1.start == o2.start)
                {
                    return o1.end - o2.end;
                }
              
                return o1.start - o2.start;
            }
        });
      
        ArrayList<Interval> ans = new ArrayList<Interval>();
        Interval newInterval = null;

        for (Interval interval : intervals)
        {
            if (newInterval == null)
            {
                newInterval = interval;
            }
            else
            {
                if (newInterval.end < interval.start)
                {
                    ans.add(newInterval);
                    newInterval = interval;
                }
                else
                {
                    newInterval.end = Math.max(newInterval.end, interval.end);
                }
            }
        }

        if (newInterval != null)
        {
            ans.add(newInterval);
        }

        return ans;
    }
}
