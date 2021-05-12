public class Solution {
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> list = new ArrayList<>();
        helper(list, root);
        return list;
    }

//calculate the index of this root passed in and put it in that index, at last return where this root was put
    private int helper(List<List<Integer>> list, TreeNode root) {
        if (root == null)
            return -1;
        int left = helper(list, root.left);
        int right = helper(list, root.right);
        int cur = Math.max(left, right) + 1;
        if (list.size() == cur)
            list.add(new ArrayList<Integer>());
        list.get(cur).add(root.val);
        return cur;
    }
}
