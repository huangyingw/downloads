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
    public int minMeetingRooms(Interval[] intervals) 
    {
        if(intervals == null || intervals.length == 0)
        {
            return 0;   
        }
        
        Arrays.sort(intervals, new Comparator<Interval>()
        {
            public int compare(Interval o1, Interval o2)
            {
                return o1.start - o2.start;
            }
        });
        
        // 用堆来管理房间的结束时间
        PriorityQueue<Integer> endTimes = new PriorityQueue<Integer>();
        endTimes.offer(intervals[0].end);
        
        for(int i = 1; i < intervals.length; i++)
        {
            // 如果当前时间段的开始时间大于最早结束的时间，则可以更新这个最早的结束时间为当前时间段的结束时间，如果小于的话，就加入一个新的结束时间，表示新的房间
            if(intervals[i].start >= endTimes.peek())
            {
                endTimes.poll();
            }
            
            endTimes.offer(intervals[i].end);
        }
        
        // 有多少结束时间就有多少房间
        return endTimes.size();
    }
}
