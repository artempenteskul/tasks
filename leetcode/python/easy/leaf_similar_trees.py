# task number - 872


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def leaf_similar(root1: TreeNode, root2: TreeNode) -> bool:

    def get_tree_leafs(root_node: TreeNode) -> list[int]:
        stack = [root_node]
        leafs = []

        while stack:
            node = stack.pop(-1)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

            if not node.left and not node.right:
                leafs.append(node.val)

        return leafs

    return get_tree_leafs(root1) == get_tree_leafs(root2)


if __name__ == '__main__':
    input_root1 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    input_root2 = TreeNode(1, left=TreeNode(3), right=TreeNode(2))
    print(f'Are trees leaf similar - {leaf_similar(input_root1, input_root2)}')  # false

    input_root1 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    input_root2 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    print(f'Are trees leaf similar - {leaf_similar(input_root1, input_root2)}')  # true
