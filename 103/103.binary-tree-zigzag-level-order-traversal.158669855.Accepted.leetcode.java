public class Solution
{
    public List<List<Integer>> zigzagLevelOrder(TreeNode root)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        traverse(root, 0, result, true);
        return result;
    }

    public void traverse(TreeNode root, int level, List<List<Integer>> result, Boolean left_to_right)
    {
        if (root == null)
        {
            return;
        }

        if (level == result.size())
        {
            result.add(new ArrayList<Integer>());
        }

        if (left_to_right)
        {
            result.get(level).add(root.val);
        }
        else
        {
            result.get(level).add(0, root.val);
        }

        traverse(root.left, level + 1, result, !left_to_right);
        traverse(root.right, level + 1, result, !left_to_right);
    }
}

