public class SummaryRanges
  {

    /** Initialize your data structure here. */

    private TreeSet<Interval> intervalSet;

    public SummaryRanges()
    {
      intervalSet = new TreeSet<Interval>(new Comparator<Interval>()
      {
        public int compare(Interval a, Interval b)
        {
          return a.start - b.start;
        }
      });
    }

    public void addNum(int val)
    {
      Interval valInterval = new Interval(val, val);
      Interval floor = intervalSet.floor(valInterval);

      if (floor != null)
      {
        if (floor.end >= val)
        {
          return;
        }
        else if (floor.end + 1 == val)
        {
          valInterval.start = floor.start;
          intervalSet.remove(floor);
        }
      }

      Interval higher = intervalSet.higher(valInterval);

      if (higher != null && higher.start == val + 1)
      {
        valInterval.end = higher.end;
        intervalSet.remove(higher);
      }

      intervalSet.add(valInterval);
    }

    public List<Interval> getIntervals()
    {
      return Arrays.asList(intervalSet.toArray(new Interval[0]));
    }
  }

