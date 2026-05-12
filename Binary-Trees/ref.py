def ref_inorder(node, result):
    if node is None:
        return result
    ref_inorder(node.left, result)
    if node.val is not None:
        result.append(node.val)
    ref_inorder(node.right, result)
    return result