# task number - 94
# topics - stack, tree, depth-first-search, binary tree


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode or None) -> list[int]:
    if not root:
        return []

    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


if __name__ == '__main__':
    input_root = TreeNode(val=1, right=TreeNode(2, left=TreeNode(3)))
    print(f'Result tree inorder traversal - {inorder_traversal(input_root)}')  # [1, 3, 2]
