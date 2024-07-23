# task number - 104


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_max_depth_dfs(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left_depth = count_max_depth_dfs(root.left)
    right_depth = count_max_depth_dfs(root.right)
    return max(left_depth, right_depth) + 1


def count_max_depth_bfs(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    depth = 0
    queue = [root]

    while queue:
        depth += 1
        level_size = len(queue)

        for i in range(level_size):
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    return depth


if __name__ == '__main__':
    root_node = TreeNode(3)
    root_node.left = TreeNode(9)
    root_node.right = TreeNode(20)
    root_node.right.left = TreeNode(15)
    root_node.right.right = TreeNode(7)

    print(count_max_depth_dfs(root_node))  # 3
