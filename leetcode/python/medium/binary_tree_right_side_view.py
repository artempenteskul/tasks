# task number - 199


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: TreeNode) -> list[int]:
    if not root:
        return []

    view = []
    queue = [root]
    current_level_val = None

    while queue:
        current_level_len = len(queue)
        for _ in range(current_level_len):
            node = queue.pop(0)
            current_level_val = node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        view.append(current_level_val)

    return view


if __name__ == '__main__':
    input_root = TreeNode(1, left=TreeNode(2, left=TreeNode(5)), right=TreeNode(3, right=TreeNode(4)))
    print(f'Right side view for input binary tree - {right_side_view(input_root)}')

    input_root = TreeNode(1, right=TreeNode(3))
    print(f'Right side view for input binary tree - {right_side_view(input_root)}')
