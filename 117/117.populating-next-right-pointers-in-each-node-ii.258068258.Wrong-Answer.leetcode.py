class Solution:
    def connect(self, root):
        head = None        # head of next layer
        previous = None    # previous non-blank node on the next layer
        current = root     # current node of current layer

        while current is not None:
            while current is not None:
                if current.left is not None:
                    if previous is not None:
                        previous.next = current.left
                    else:
                        # previous is None, means current is layer's first node, so update head to current.left, means next layer's first node
                        head = current.left
                    previous = current.left
                if current.right is not None:
                    if previous is not None:
                        previous.next = current.right
                    else:
                        head = current.right
                    previous = current.right
                # Lead to current layer's next
                current = current.next
            # Swtich to next layer
            current = head
            head = None
            previous = None

