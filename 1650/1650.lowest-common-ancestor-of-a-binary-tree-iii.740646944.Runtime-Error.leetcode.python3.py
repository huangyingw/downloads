class Solution:
    def lowestCommonAncestor(self, a, b):
        pointerA, pointerB = a, b
        while pointerA != pointerB:
            pointerA = pointerA.parent if pointerA else b
            pointerB = pointerB.parent if pointerA else a
        return pointerA

