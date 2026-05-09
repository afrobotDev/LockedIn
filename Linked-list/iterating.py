from linked_lists import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node: 
            yield node 
            node = node.next

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)


