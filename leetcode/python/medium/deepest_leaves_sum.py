# task number - 1302
# topics - bfs, binary tree


class TreeNode:
    def __init__(self, val: int = 0,  left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def deepest_leafs_sum(root: TreeNode or None) -> int:
    if not root:
        return 0

    deepest_sum = 0
    queue = [root]

    while queue:
        deepest_sum = 0
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.pop(0)

            deepest_sum += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return deepest_sum


if __name__ == '__main__':
    input_root = TreeNode(1, left=TreeNode(2, left=TreeNode(4, left=TreeNode(7)), right=TreeNode(5)), right=TreeNode(3, right=TreeNode(6, right=TreeNode(8))))
    print(f'Result of deepest leafs sum - {deepest_leafs_sum(input_root)}')
