# task number - 226


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(root: TreeNode) -> TreeNode or None:
    if not root:
        return None

    stack = [root]

    while stack:
        node = stack.pop(-1)
        node.left, node.right = node.right, node.left

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return root
