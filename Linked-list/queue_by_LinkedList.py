from linked_lists import Node


class LLQueue:
    # remove first element from the list and return it
    def remove_from_head(self):
        if self.head is None:
            return None
        tobe_removed = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        tobe_removed.next = None 
        return tobe_removed

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(str(node.val))
        return " <- ".join(nodes)

