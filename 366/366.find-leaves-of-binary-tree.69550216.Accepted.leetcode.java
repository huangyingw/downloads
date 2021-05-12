  public class Solution
  {
    public List<List<Integer>> findLeaves(TreeNode root)
    {
      List<List<Integer>> result = new ArrayList<>();
      dfs(result, root);
      return result;
    }
    private int dfs(List<List<Integer>> result, TreeNode root)
    {
      if (root == null)
      {
        return -1;
      }

      int depth = Math.max(dfs(result, root.left), dfs(result, root.right)) + 1;

      if (result.size() == depth)
      {
        result.add(new ArrayList<Integer>());
      }

      result.get(depth).add(root.val);
      return depth;
    }
  }

