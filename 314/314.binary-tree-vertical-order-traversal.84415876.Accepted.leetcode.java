/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class Solution 
{  
    class TreeColumnNode 
    {  
        TreeNode treeNode;  
        int column;  
    
        TreeColumnNode(TreeNode treeNode, int column) 
        {  
            this.treeNode = treeNode;  
            this.column = column;  
        }  
    } 
    
    public List<List<Integer>> verticalOrder(TreeNode root) 
    {  
        List<List<Integer>> results = new ArrayList<>();  
        
        if (root == null) 
        {
            return results;  
        }
        
        Map<Integer, List<Integer>> map = new HashMap<>();  
        LinkedList<TreeColumnNode> queue = new LinkedList<>();  
        queue.add(new TreeColumnNode(root, 0));  
        
        while (!queue.isEmpty()) 
        {  
            TreeColumnNode node = queue.remove();  
            List<Integer> list = map.get(node.column);  
            
            if (list == null) 
            {  
                list = new ArrayList<>();  
                map.put(node.column, list);  
            }  
            
            list.add(node.treeNode.val);  
            
            if (node.treeNode.left != null)
            {
                queue.add(new TreeColumnNode(node.treeNode.left, node.column - 1));  
            }
            
            if (node.treeNode.right != null) 
            {
                queue.add(new TreeColumnNode(node.treeNode.right, node.column + 1));  
            }
        }  
        
        List<Integer> columns = new ArrayList<>(map.keySet());  
        Collections.sort(columns);  
        
        for(int i = 0; i < columns.size(); i++) 
        {  
            results.add(map.get(columns.get(i)));  
        }  
        
        return results;  
    }  
}
