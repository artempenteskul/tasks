# task number - 108


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(nums: list[int]) -> TreeNode or None:
    if not nums:
        return None

    mid = len(nums) // 2

    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid + 1:])

    return root


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)


if __name__ == '__main__':
    input_nums = [-10, -5, -3, 0, 5, 7, 9]
    head = sorted_array_to_bst(input_nums)

    print('Inorder traversal of the constructed BST: ')
    inorder_traversal(head)
