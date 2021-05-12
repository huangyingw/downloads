public class Solution
{
    public boolean canAttendMeetings(Interval[] intervals)
    {
        if(intervals == null || intervals.length == 0)
        {
            return true;
        }
      
        Arrays.sort(intervals, new Comparator<Interval>()
        {
            public int compare(Interval a, Interval b)
            {
                if(a.start == b.start)
                {
                    return a.end - b.end;
                }
                
                return a.start - b.start;
            }
        }
        );
        
        int end = intervals[0].end;

        for (int i = 1; i < intervals.length; i++)
        {
            if (intervals[i].start < end)
            {
                return false;
            }

            end = Math.max(end, intervals[i].end);
        }

        return true;
    }
}
