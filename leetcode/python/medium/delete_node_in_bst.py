# task number - 450


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def delete_node(root: TreeNode, key: int) -> TreeNode or None:
    if not root:
        return root

    if key > root.val:
        root.right = delete_node(root.right, key)
    elif key < root.val:
        root.left = delete_node(root.left, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # find the min from right subtree
        cur = root.right
        while cur.left:
            cur = cur.left

        root.val = cur.val
        root.right = delete_node(root.right, root.val)

    return root
