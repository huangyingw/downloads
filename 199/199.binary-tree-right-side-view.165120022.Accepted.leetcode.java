public class Solution
{
    public List<Integer> rightSideView(TreeNode root)
    {
        Map<Integer, Integer> treeMap = new TreeMap<Integer, Integer>();
        inorderTraversal(treeMap, root, 0);
        return new ArrayList<Integer>(treeMap.values());
    }

    public void inorderTraversal(Map<Integer, Integer> treeMap, TreeNode root, int level)
    {
        if (root == null)
        {
            return;
        }

        inorderTraversal(treeMap, root.left, level + 1);
        treeMap.put(level, root.val);
        inorderTraversal(treeMap, root.right, level + 1);
    }
}

