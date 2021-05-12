class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        pA = headA
        pB = headB
        tailA = None
        tailB = None

        while True:
            if not pA:
                pA = headB

            if not pB:
                pB = headA

            if not pA.next:
                tailA = pA

            if not pB.next:
                tailB = pB

            if pA == pB:
                return pA

            if tailA and tailB and tailA != tailB:
                return None

            pA = pA.next
            pB = pB.next

