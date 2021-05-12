class Solution:
    def cloneGraph(self, node):
        def dfs(input, map):
            if input in map:
                return map[input]
            output = Node(input.val, [])
            map[input] = output
            for neighbor in input.neighbors:
                output.neighbors += [dfs(neighbor, map)]
            return output
        if node == None:
            return None
        return dfs(node, {})

