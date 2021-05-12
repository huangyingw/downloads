  public class Solution
  {
    HashMap<String, PriorityQueue<String>> map =
      new HashMap<String, PriorityQueue<String>>();
    List<String> result = new LinkedList<>();
    public List<String> findItinerary(String[][] tickets)
    {
      for (String[] ticket : tickets)
      {
        if (!map.containsKey(ticket[0]))
        {
          PriorityQueue<String> q = new PriorityQueue<String>();
          map.put(ticket[0], q);
        }

        map.get(ticket[0]).offer(ticket[1]);
      }

      dfs("JFK");
      return result;
    }
    public void dfs(String s)
    {
      PriorityQueue<String> q = map.get(s);

      while (q != null && !q.isEmpty())
      {
        dfs(q.poll());
      }

      ((LinkedList<String>) result).addFirst(s);
    }
  }

