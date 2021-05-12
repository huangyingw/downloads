class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if None == root:
            return []
        reflist1 = [root]
        while True:
            reflist2 = []
            for i in range(0, len(reflist1)):
                cur = reflist1[i]
                if None != cur.left:
                    reflist2.append(cur.left)
                if None != cur.right:
                    reflist2.append(cur.right)
            if 0 == len(reflist2):
                break
            len_l = len(reflist2)
            for i in range(0, len_l - 1):
                reflist2[i].next = reflist2[i + 1]
            reflist2[len_l - 1].next = None
            reflist1 = reflist2

