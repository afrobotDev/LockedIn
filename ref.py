from redblack_trees import RBNode, RBTree


def ref_implementation(tree, val):
    tree.insert(val)


def ref_inorder(node, result):
    if node is None:
        return result
    if node.val is None:
        return result
    result = ref_inorder(node.left, result)
    result.append(node.val)
    result = ref_inorder(node.right, result)
    return result
