# task number - 1161


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def max_level_sum(root: 'TreeNode') -> int:
    level_max_sum = float('-inf')
    level_max_num = 1
    queue = [root]
    cur_level_sum = 0
    cur_level_num = 1

    while queue:
        level_len = len(queue)
        for _ in range(level_len):
            node = queue.pop(0)
            cur_level_sum += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        if cur_level_sum > level_max_sum:
            level_max_sum = cur_level_sum
            level_max_num = cur_level_num

        cur_level_num += 1
        cur_level_sum = 0

    return level_max_num


if __name__ == '__main__':
    input_tree = TreeNode(1, left=TreeNode(7, left=TreeNode(7), right=TreeNode(-8)), right=TreeNode(0))
    print(f'Maximum level sum for input binary tree: {max_level_sum(input_tree)}')  # 2
