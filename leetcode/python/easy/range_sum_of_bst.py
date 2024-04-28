# task number - 938


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def range_sum_bst(root: TreeNode, low: int, high: int) -> int:
    sum_bst = 0

    if not root:
        return sum_bst

    if low <= root.val <= high:
        sum_bst += root.val

    return sum_bst + range_sum_bst(root.left, low, high) + range_sum_bst(root.right, low, high)


if __name__ == '__main__':
    input_left = TreeNode(5, left=TreeNode(3), right=TreeNode(7))
    input_right = TreeNode(15, right=TreeNode(18))
    input_root = TreeNode(10, left=input_left, right=input_right)
    input_low = 7
    input_high = 15

    print(f'Range sum for input bst with range [{input_low}:{input_high}] - {range_sum_bst(input_root, input_low, input_high)}')  # 32
