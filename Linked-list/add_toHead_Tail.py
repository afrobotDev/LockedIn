from linked_lists import Node

class LinkedList:
    # add a new node to the head
    def add_to_head(self, node):
        if not self.head:
            self.tail = node

        node.next = self.head
        self.head = node

    # add_to_tail adds a new node to the end of the list
    def add_to_tail(self, node):
        if not self.head:
            self.head = node            
            self.tail = node
            return 
        self.tail.next = node
        self.tail = node


    def __init__(self):
        self.head = None
        self.tail = None


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


