public class Solution {
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        Queue<Integer> klist = new LinkedList<Integer>();
        Stack<TreeNode> stk = new Stack<TreeNode>();
        // 迭代中序遍历二叉搜索树的代码
        while(root != null){
            stk.push(root);
            root = root.left;
        }
        while(!stk.isEmpty()){
            TreeNode curr = stk.pop();
            // 维护一个大小为k的队列
            // 队列不到k时直接加入
            if(klist.size() < k){
                klist.offer(curr.val);
            } else {
            // 队列到k时，判断下新的数是否更近，更近就加入队列并去掉队头
                int first = klist.peek();
                if(Math.abs(first - target) > Math.abs(curr.val - target)){
                    klist.poll();
                    klist.offer(curr.val);
                } else {
                // 如果不是更近则直接退出，后面的数只会更大
                    break;
                }
            }
            // 中序遍历的代码
            if(curr.right != null){
                curr = curr.right;
                while(curr != null){
                    stk.push(curr);
                    curr = curr.left;
                }
            }
        }
        // 强制转换成List，是用LinkedList实现的所以可以转换
        return (List<Integer>)klist;
    }
}
