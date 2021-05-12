import gc


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        savedA, savedB = headA, headB
        while headA != headB:
            headA = savedB if not headA else headA.next
            headB = savedA if not headB else headB.next
        gc.collect()
        return headA

