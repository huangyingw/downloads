from sets import Set


class Solution(object):
    def alienOrder(self, words):
        if not words:
            return ""

        if len(words) == 1:
            return "".join([s for s in Set(words[0])])

        # len(words) >=2
        adj_dict = self.build_graph(words)
        visit_dict = dict([(k, 0) for k in adj_dict.keys()])
        res = []
        self.valid = True

        for c in adj_dict.keys():
            self.topo_sort(c, visit_dict, adj_dict, res)
        return "".join([s for s in res]) if self.valid else ""

    def build_graph(self, words):
        adj_dict = {}

        def add_node(c):
            if adj_dict.get(c, None) == None:
                adj_dict[c] = {}

        def add_link(src, des):
            adj_dict[src][des] = None

        for i in xrange(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            start2 = 0
            for j in xrange(min(len(w1), len(w2))):
                if w1[j] == w2[j]:
                    add_node(w1[j])
                else:
                    add_node(w1[j])
                    add_node(w2[j])
                    add_link(w2[j], w1[j])
                    start2 = j + 1
                    break
            for j in xrange(start2, len(w1)):
                add_node(w1[j])
            for j in xrange(start2, len(w2)):
                add_node(w2[j])

        return adj_dict

    def topo_sort(self, c, visit_dict, adj_dict, res):
        if self.valid and not visit_dict[c]:
            visit_dict[c] = 1
            for adj_c in adj_dict[c].keys():
                if visit_dict[adj_c] == 1:
                    self.valid = False
                    return
                if not visit_dict[adj_c] and self.valid:
                    self.topo_sort(adj_c, visit_dict, adj_dict, res)

            visit_dict[c] = 2
            res.append(c)

