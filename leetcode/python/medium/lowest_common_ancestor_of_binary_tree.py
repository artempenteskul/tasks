# task number - 236


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode, ancestor: int = None) -> 'TreeNode' or None:
    if root is None:
        return None

    if root.val == p.val or root.val == q.val:
        return root

    left_lca = common_ancestor(root.left, p, q)
    right_lca = common_ancestor(root.right, p, q)

    if left_lca is not None and right_lca is not None:
        return root

    if left_lca is not None:
        return left_lca

    return right_lca


if __name__ == '__main__':
    input_p = TreeNode(5)
    input_q = TreeNode(1)
    input_root = TreeNode(3, left=TreeNode(5, left=TreeNode(6)), right=TreeNode(1, left=TreeNode(0), right=TreeNode(8)))
    print(f'Lowest common ancestor for input p and q is {common_ancestor(input_root, input_p, input_q).val}')  # 3
