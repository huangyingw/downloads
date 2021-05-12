public class Solution
{
    public List<Interval> insert(List<Interval> intervals, Interval newInterval)
    {
        List<Interval> result = new ArrayList<Interval>();

        if (intervals == null || intervals.size() == 0)
        {
            result.add(newInterval);
            return result;
        }

        for (Interval interval : intervals)
        {
            if (interval.end < newInterval.start)
            {
                result.add(interval);
            }
            else if (interval.start > newInterval.end)
            {
                result.add(newInterval);
                newInterval = interval;
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
