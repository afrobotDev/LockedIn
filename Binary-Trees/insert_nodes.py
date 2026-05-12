class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


    def insert(self, val):
            if not self.val:
                self.val = val
                return
            elif self.val == val:
                return
            elif self.val > val and not self.left:
                self.left = BSTNode(val)
                return
            elif self.val > val and self.left:
                self.left.insert(val)
                return
            else:
                if self.right:
                    self.right.insert(val)
                    return
                self.right = BSTNode(val)
                return
