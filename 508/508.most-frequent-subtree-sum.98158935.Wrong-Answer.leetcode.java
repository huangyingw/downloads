public class Solution
{
    public int[] findFrequentTreeSum(TreeNode root)
    {
        Map<Integer, Integer> map = new HashMap<>();
        treeSum(map, root);
        int max = Integer.MIN_VALUE;
        int count = 0;

        
        int[] res = new int[count];
        count = 0;

        for (int key : map.keySet())
        {
            if (map.get(key) == max)
            {
                res[count++] = key;
            }
        }

        return res;
    }

    public int treeSum(Map<Integer, Integer> map, TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }

        root.val = root.val + treeSum(map, root.left) + treeSum(map, root.right);

        if (map.containsKey(root.val))
        {
            map.put(root.val, map.get(root.val) + 1);
        }
        else
        {
            map.put(root.val, 1);
        }

        return root.val;
    }
}
