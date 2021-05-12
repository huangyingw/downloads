import json


class Codec:

    def serialize(self, root):
        if not root:
            return 'null'
        nodes = collections.deque([root])
        maps = collections.deque([{'v': root.val}])
        tree = maps[0]
        while nodes:
            frontNode = nodes.popleft()
            frontMap = maps.popleft()
            if frontNode.left:
                frontMap['l'] = {'v': frontNode.left.val}
                nodes.append(frontNode.left)
                maps.append(frontMap['l'])
            if frontNode.right:
                frontMap['r'] = {'v': frontNode.right.val}
                nodes.append(frontNode.right)
                maps.append(frontMap['r'])
        return json.dumps(tree)

    def deserialize(self, data):
        tree = json.loads(data)
        if not tree:
            return None
        root = TreeNode(tree['v'])
        maps = collections.deque([tree])
        nodes = collections.deque([root])
        while nodes:
            frontNode = nodes.popleft()
            frontMap = maps.popleft()
            left, right = frontMap.get('l'), frontMap.get('r')
            if left:
                frontNode.left = TreeNode(left['v'])
                maps.append(left)
                nodes.append(frontNode.left)
            if right:
                frontNode.right = TreeNode(right['v'])
                maps.append(right)
                nodes.append(frontNode.right)
        return root

