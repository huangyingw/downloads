/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution 
{  
    private ListNode reverse(ListNode head) 
    {  
        ListNode prev = null;  
        
        while (head != null) 
        {  
            ListNode temp = head.next;  
            head.next = prev;  
            prev = head;  
            head = temp;  
        }  
        
        return prev;  
    }
    
    public ListNode plusOne(ListNode head) 
    {  
        if (head == null) 
        {   
            return null;  
        }
        
        head = reverse(head);  
        head.val++;  
        ListNode current = head;  
        
        while (current != null && current.val >= 10)
        {
            current.val -= 10;
            
            if (current.next != null)
            {
                current.next.val++;    
            }
            else
            {
                current.next = new ListNode(1);
            }
            
            current = current.next;
        }
        
        return reverse(head);  
    }  
}
