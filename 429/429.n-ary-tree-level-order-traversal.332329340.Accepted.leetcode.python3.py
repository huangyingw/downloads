class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            next_level = []
            cur_level_val = []
            for cur_node in queue:
                cur_level_val.append(cur_node.val)
                if cur_node.children:
                    next_level.extend(cur_node.children)
            queue = next_level
            res.append(cur_level_val)
        return res

