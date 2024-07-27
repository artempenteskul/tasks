# task number - 1372


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def longest_zigzag(root: TreeNode, last_turn: str = '', current_len: int = 0) -> int:
    if not root:
        return current_len

    if not last_turn:
        left_len, right_len = 0, 0

    elif last_turn == 'left':
        left_len = 0
        right_len = current_len + 1

    else:
        left_len = current_len + 1
        right_len = 0

    return max(longest_zigzag(root.left, 'left', left_len), longest_zigzag(root.right, 'right', right_len))


if __name__ == '__main__':
    input_root = TreeNode(1, left=TreeNode(1, right=TreeNode(1)), right=TreeNode(1, right=TreeNode(1)))
    print(f'Longest zigzag path for input binary tree: {longest_zigzag(input_root)}')  # 2

    input_root = TreeNode(1)
    print(f'Longest zigzag path for input binary tree - {longest_zigzag(input_root)}')  # 0

    subtree_root = TreeNode(1, left=TreeNode(1, right=TreeNode(1, right=TreeNode(1))), right=TreeNode(1))
    input_root = TreeNode(1, right=TreeNode(1, left=TreeNode(1), right=subtree_root))
    print(f'Longest zigzag path for input binary tree - {longest_zigzag(input_root)}')  # 3
