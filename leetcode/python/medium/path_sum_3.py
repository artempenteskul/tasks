# task number - 437


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root: TreeNode, target: int, current_paths: list = None) -> int:
    if not root:
        return 0

    if current_paths is None:
        target_path_qty = 1 if root.val == target else 0
        current_paths = [root.val]
    else:
        current_paths = [x + root.val for x in current_paths] + [root.val]
        target_path_qty = current_paths.count(target)

    return target_path_qty + path_sum(root.left, target, current_paths) + path_sum(root.right, target, current_paths)


if __name__ == '__main__':
    input_subtree_left = TreeNode(5, left=TreeNode(3, left=TreeNode(3), right=TreeNode(-2)), right=TreeNode(2, right=TreeNode(1)))
    input_subtree_right = TreeNode(-3, right=TreeNode(11))
    input_root = TreeNode(10, left=input_subtree_left, right=input_subtree_right)

    input_target = 8

    print(f'Path sum for target {input_target} for input binary tree: {path_sum(input_root, input_target)}')  # 3

    ###

    input_root = TreeNode(1)
    input_target = 1
    print(f'Path sum for target {input_target} for input binary tree: {path_sum(input_root, input_target)}')  # 1
