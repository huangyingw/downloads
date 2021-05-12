public class Solution
{
    public List<Interval> insert(List<Interval> intervals, Interval newInterval)
    {
        List<Interval> result = new ArrayList<Interval>();
        
        for (int i = 0; i < intervals.size(); i++)
        {
            Interval interval = intervals.get(i);

            if (newInterval.end < interval.start)
            {
                result.add(newInterval);
            }
            else if (newInterval.start > interval.end)
            {
                result.add(interval);
            }
            else
            {
                newInterval.start = Math.min(newInterval.start, interval.start);
                newInterval.end = Math.max(newInterval.end, interval.end);
            }
        }

        result.add(newInterval);
        return result;
    }
}
