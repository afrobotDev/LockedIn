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
        elif self.val > val:
            if not self.left:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)

def ref_implementation(bst, val):
    bst.insert(val)

def ref_inorder(bst, lst):
    if bst:
        ref_inorder(bst.left, lst)
        lst.append(bst.val)
        ref_inorder(bst.right, lst)
    return lst