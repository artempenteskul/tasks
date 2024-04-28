# task number - 700


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search_in_bst(root: TreeNode, val: int) -> TreeNode or None:
    if root.val == val:
        return root

    if root.val > val and root.left:
        return search_in_bst(root.left, val)
    elif root.val < val and root.right:
        return search_in_bst(root.right, val)
    else:
        return None


if __name__ == '__main__':
    input_left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    input_right = TreeNode(7)
    input_root = TreeNode(4, left=input_left, right=input_right)

    search_result_root = search_in_bst(input_root, val=2)
    print(f'Search result bst root val - {search_result_root.val}')  # 2
