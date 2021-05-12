import gc


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        savedA, savedB = headA, headB
        len_diff = 0
        while headA.next:
            len_diff += 1
            headA = headA.next
        while headB.next:
            len_diff -= 1
            headB = headB.next
        if headA != headB:
            return
        headA, headB = savedA, savedB
        while len_diff != 0:
            if len_diff > 0:
                headA = headA.next
                len_diff -= 1
            else:
                headB = headB.next
                len_diff += 1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        gc.collect()
        return headA

