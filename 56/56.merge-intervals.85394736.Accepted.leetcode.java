/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution 
{
    public List<Interval> merge(List<Interval> intervals) 
    {
        Collections.sort(intervals, new Comparator<Interval>() 
        {
            @Override
            public int compare(Interval i1, Interval i2) 
            {
                if (i1.start == i2.start) 
                {
                    return i1.end - i2.end;
                }

                return i1.start - i2.start;
            }
        });
      
        ArrayList<Interval> ans = new ArrayList<Interval>();
        Interval newInterval = null;

        for(Interval interval : intervals)
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
                    newInterval = new Interval(newInterval.start, Math.max(newInterval.end, interval.end));
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
