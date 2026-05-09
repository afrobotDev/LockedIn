class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def size(self):
        return len(self.items)
    
    def search_and_remove(self, item):
        self.items.remove(item) if item in self.items else return None
        return item

    def __rpr__(self):
        return f"[{', '.join(self.items)}]"

