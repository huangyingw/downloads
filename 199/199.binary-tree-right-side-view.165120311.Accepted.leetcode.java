public class Solution
{
    public List<Integer> rightSideView(TreeNode root)
    {
        Map<Integer, Integer> treeMap = new TreeMap<Integer, Integer>();
        traversal(treeMap, root, 0);
        return new ArrayList<Integer>(treeMap.values());
    }

    public void traversal(Map<Integer, Integer> treeMap, TreeNode root, int level)
    {
        if (root == null)
        {
            return;
        }

        traversal(treeMap, root.left, level + 1);
        treeMap.put(level, root.val);
        traversal(treeMap, root.right, level + 1);
    }
}

