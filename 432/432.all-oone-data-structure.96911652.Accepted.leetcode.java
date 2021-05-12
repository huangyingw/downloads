public class AllOne
{

    private ValueNode head;// largest
    private ValueNode tail;// smallest
    private Map<String, ValueNode> elements;

    /** Initialize your data structure here. */
    public AllOne()
    {
        head = null;
        tail = null;
        this.elements = new HashMap<>();
    }

    /**
     * Inserts a new key <key> with value 1. Or increments an existing key by 1.
     */
    public void inc(String key)
    {
        // if no element in the map, add the element to tail with value 1
        if (!elements.containsKey(key))
        {
            if (tail == null || tail.value > 1)
            {
                ValueNode prevTail = null;

                if (tail != null)
                {
                    prevTail = tail;
                }

                tail = new ValueNode(1, key);

                if (head == null)
                {
                    head = tail;
                }

                if (prevTail != null)
                {
                    prevTail.next = tail;
                    tail.prev = prevTail;
                }
            }
            else
            {
                tail.keys.add(key);
            }

            elements.put(key, tail);
        }
        else
        {
            ValueNode curr = elements.get(key);

            if (curr.prev != null && curr.prev.value == curr.value + 1)
            {
                curr.prev.keys.add(key);
                elements.put(key, curr.prev);
            }
            else
            {
                ValueNode prev = new ValueNode(curr.value + 1, key);

                if (curr.prev != null)
                {
                    ValueNode prevprev = curr.prev;
                    prevprev.next = prev;
                    prev.prev = prevprev;
                    // which means curr is head
                }
                else
                {
                    head = prev;
                }

                curr.prev = prev;
                prev.next = curr;
                elements.put(key, prev);
            }

            curr.keys.remove(key);

            if (!checkEmpty(curr))
            {
                curr.updateOneKey(key);
            }
        }
    }

    /**
     * Decrements an existing key by 1. If Key's value is 1, remove it from the
     * data structure.
     */
    public void dec(String key)
    {
        if (elements.containsKey(key))
        {
            ValueNode curr = elements.get(key);

            if (curr.next != null && curr.next.value == curr.value - 1)
            {
                curr.next.keys.add(key);
                elements.put(key, curr.next);
            }
            else
            {
                if (curr.value > 1)
                {
                    ValueNode next = new ValueNode(curr.value - 1, key);

                    if (curr.next != null)
                    {
                        ValueNode nextnext = curr.next;
                        next.next = nextnext;
                        nextnext.prev = next;
                    }
                    else
                    {
                        tail = next;
                    }

                    curr.next = next;
                    next.prev = curr;
                    elements.put(key, next);
                }
                else
                {
                    elements.remove(key);
                }
            }

            curr.keys.remove(key);

            if (!checkEmpty(curr))
            {
                curr.updateOneKey(key);
            }
        }
    }

    /** Returns one of the keys with maximal value. */
    public String getMaxKey()
    {
        return head != null ? head.oneKey : "";
    }

    /** Returns one of the keys with Minimal value. */
    public String getMinKey()
    {
        return tail != null ? tail.oneKey : "";
    }

    private boolean checkEmpty(ValueNode node)
    {
        if (node.keys.isEmpty())
        {
            if (node == head)
            {
                head = node.next;
                node.next.prev = null;
            }
            else if (node == tail)
            {
                tail = node.prev;
                node.prev.next = null;
            }
            else
            {
                node.prev.next = node.next;
                node.next.prev = node.prev;
            }

            node = null;
            return true;
        }
        else
        {
            return false;
        }
    }

    // Doubly linked list node
    private class ValueNode
    {
        int value;
        Set<String> keys;
        ValueNode prev;
        ValueNode next;
        String oneKey; // any key with the value

        public ValueNode(int value, String key)
        {
            this.value = value;
            keys = new HashSet<>();
            keys.add(key);
            oneKey = key;
            prev = null;
            next = null;
        }

        public void updateOneKey(String key)
        {
            if (oneKey.equals(key))
            {
                Iterator<String> it = keys.iterator();
                oneKey = it.next();
            }
        }
    }
}
