import json


class Codec:

    def serialize(self, root):
        def tuplify(root):
            return root and (root.val, tuplify(root.left), tuplify(root.right))
        return json.dumps(tuplify(root))

    def deserialize(self, data):
        def detuplify(t):
            if t:
                root = TreeNode(t[0])
                root.left = detuplify(t[1])
                root.right = detuplify(t[2])
                return root
        return detuplify(json.loads(data))

