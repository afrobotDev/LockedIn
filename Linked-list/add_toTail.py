from linked_lists import Node

class LinkedList:
    # add_to_tail adds a new node to the end of the list
    def add_to_tail(self, node):
        if not self.head:
            self.head = node 
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = node


    def __init__(self):
        self.head = None


    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)


