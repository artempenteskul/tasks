# task number - 101
# topics - tree, depth-first-search, breadth-first-search, binary tree


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):
    if not root:
        return True

    def is_mirror(root1: TreeNode or None, root2: TreeNode or None) -> bool:
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        return (root1.val == root2.val and
                is_mirror(root1.left, root2.right) and
                is_mirror(root1.right, root2.left))

    return is_mirror(root.left, root.right)


if __name__ == '__main__':
    input_root = TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)), right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)))
    print(f'Is tree symmetric - {is_symmetric(input_root)}')  # true

    input_root = TreeNode(1, left=TreeNode(2, right=TreeNode(3)), right=TreeNode(2, right=TreeNode(3)))
    print(f'Is tree symmetric - {is_symmetric(input_root)}')  # false
