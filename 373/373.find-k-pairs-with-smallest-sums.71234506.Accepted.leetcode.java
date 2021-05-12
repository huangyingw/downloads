  public class Solution
  {
    public List<int[]> kSmallestPairs(final int[] nums1, final int[] nums2,
                                      int k)
    {
      List<int[]> res = new ArrayList<>();

      if (nums1 == null || nums1.length == 0 || nums2 == null
          || nums2.length == 0)
      {
        return res;
      }

      class Pair
      {
        int x;
        int y;
        Pair(int x, int y)
        {
          this.x = x;
          this.y = y;
        }
      }

      Comparator<Pair> comp = new Comparator<Pair>()
      {
        @Override
        public int compare(Pair p1, Pair p2)
        {
          return nums1[p1.x] + nums2[p1.y] - nums1[p2.x]
                 - nums2[p2.y];
        }
      };
      PriorityQueue<Pair> queue = new PriorityQueue<Pair>(k, comp);
      boolean[][] visited = new boolean[nums1.length][nums2.length];
      queue.offer(new Pair(0, 0));
      visited[0][0] = true;
      int[][] close = new int[][] { { 0, 1 }, { 1, 0 } };

      while (k > 0 && !queue.isEmpty())
      {
        k-- ;
        Pair p = queue.poll();
        res.add(new int[] { nums1[p.x], nums2[p.y] });

        for (int i = 0; i < 2; i++)
        {
          int tx = p.x + close[i][0];
          int ty = p.y + close[i][1];

          if (tx < nums1.length && ty < nums2.length
              && !visited[tx][ty])
          {
            queue.offer(new Pair(tx, ty));
            visited[tx][ty] = true;
          }
        }
      }

      return res;
    }
  }

