# task number - 543
# topics - tree, dfs, binary tree


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def binary_tree_diameter(root: TreeNode = None) -> int:
    res = 0

    def dfs(curr: TreeNode = None) -> int:
        nonlocal res

        if not curr:
            return 0

        left = dfs(curr.left)
        right = dfs(curr.right)

        res = max(res, left + right)

        return 1 + max(left, right)

    dfs(root)

    return res


if __name__ == '__main__':
    input_root = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3))
    print(f'Binary tree diameter for input root - {binary_tree_diameter(input_root)}')  # 3

    input_root = TreeNode(1, left=TreeNode(2))
    print(f'Binary tree diameter for input root - {binary_tree_diameter(input_root)}')  # 1
