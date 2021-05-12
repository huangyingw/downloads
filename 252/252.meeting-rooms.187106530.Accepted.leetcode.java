public class Solution
{
    public boolean canAttendMeetings(Interval[] intervals)
    {
        if (intervals.length == 0)
        {
            return true;
        }

        Arrays.sort(intervals, new Comparator<Interval>()
        {
            public int compare(Interval i1, Interval i2)
            {
                return i1.start - i2.start;
            }
        });
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

