"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
"""


class Solution(object):
    def copyRandomList(self, head):

        if not head:
            return head

        ptr = head
        while ptr:

            new_node = RandomListNode(ptr.label)

            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next
        ptr = head

        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        ptr_old_list = head
        ptr_new_list = head.next
        head_old = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_old

