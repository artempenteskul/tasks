# task number - 1448


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_good_nodes(root: TreeNode, current_max: int = None) -> int:
    if not root:
        return 0

    if current_max is not None:
        if current_max > root.val:
            return count_good_nodes(root.left, current_max) + count_good_nodes(root.right, current_max)
        else:
            return 1 + count_good_nodes(root.left, root.val) + count_good_nodes(root.right, root.val)

    return 1 + count_good_nodes(root.left, current_max=root.val) + count_good_nodes(root.right, current_max=root.val)


if __name__ == '__main__':
    input_root = TreeNode(3, left=TreeNode(1, left=TreeNode(3)), right=TreeNode(4, left=TreeNode(1), right=TreeNode(5)))
    print(f'Good nodes quantity for input root - {count_good_nodes(input_root)}')
