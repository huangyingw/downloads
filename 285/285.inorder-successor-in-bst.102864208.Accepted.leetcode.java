public class Solution
{
    public TreeNode minValue(TreeNode root)
    {
        TreeNode nav = root;

        while (nav.left != null)
        {
            nav = nav.left;
        }

        return nav;
    }
 
    TreeNode inorderSuccessor(TreeNode cur, TreeNode target)
    {
        if (target.right != null)
        {
            return minValue(target.right);
        }

        TreeNode pre = null;

        while (cur != null)
        {
            if (cur.val > target.val)
            {
                pre = cur;
                cur = cur.left;
            }
            else if (cur.val < target.val)
            {
                cur = cur.right;
            }
            else
            {
                break;
            }
        }

        return pre;
    }
}
