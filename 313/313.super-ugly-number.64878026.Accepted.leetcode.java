  public class Solution
  {
    class Node implements Comparable<Node>
    {
      int index;
      int val;
      int prime;
      Node(int index, int val, int prime)
      {
        this.val = val;
        this.index = index;
        this.prime = prime;
      }
      public int compareTo(Node x)
      {
        return this.val - x.val;
      }
    }
    public int nthSuperUglyNumber(int n, int[] primes)
    {
      int[] ugly_number = new int[n];
      ugly_number[0] = 1;
      PriorityQueue<Node> q = new PriorityQueue<Node>();

      for (int i = 0; i < primes.length; i++)
      {
        q.add(new Node(0, primes[i], primes[i]));
      }

      for (int i = 1; i < n; i++)
      {
        Node cur = q.peek();
        ugly_number[i] = cur.val;

        do
        {
          cur = q.poll();
          cur.val = ugly_number[ ++cur.index] * cur.prime;
          q.add(cur);
        }
        while (!q.isEmpty() && q.peek().val == ugly_number[i]);
      }

      return ugly_number[n - 1];
    }
  }

