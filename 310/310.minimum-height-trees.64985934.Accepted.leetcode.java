  public class Solution
  {
    public List<Integer> findMinHeightTrees(int n, int[][] edges)
    {
      List<Integer> result = new ArrayList<>();

      if (n <= 0)
      {
        return result;
      }

      // Corner case: there is a single node and no edge at all
      if (n == 1 && edges.length == 0)
      {
        result.add(0);
        return result;
      }

      // Step 1: construct the graph
      List<Set<Integer>> adjList = new ArrayList<>();

      for (int i = 0; i < n; i++)
      {
        adjList.add(new HashSet<>());
      }

      for (int[] edge : edges)
      {
        int from = edge[0];
        int to = edge[1];
        adjList.get(from).add(to);
        adjList.get(to).add(from);
      }

      // Remove leaf nodes
      List<Integer> leaves = new ArrayList<>();

      for (int i = 0; i < n; i++)
      {
        if (adjList.get(i).size() == 1)
        {
          leaves.add(i);
        }
      }

      while (n > 2)
      {
        // identify and remove all leaf nodes
        n -= leaves.size();
        List<Integer> newLeaves = new ArrayList<>();

        for (int leaf : leaves)
        {
          int neighbor = adjList.get(leaf).iterator().next();
          adjList.get(neighbor).remove(leaf);

          if (adjList.get(neighbor).size() == 1)
          {
            newLeaves.add(neighbor);
          }
        }

        leaves = newLeaves;
      }

      return leaves;
    }
  }

